# v0.1.0
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
from dataclasses import dataclass

STANCE_SUPPORTS = 1
STANCE_CONTRADICTS = 2


@gl.contract_interface
class ICorroborate:
    class View:
        def is_corroborated(
            self,
            case_id: u256,
            expected_definition_hash: str,
            expected_finalization_hash: str,
            required_side: u8,
        ) -> bool: ...
    class Write:
        pass


@allow_storage
@dataclass
class ExecutionReceipt:
    caller: Address
    case_id: u256
    required_side: u8
    definition_hash: str
    finalization_hash: str
    action_hash: str
    payload_hash: str


class EvidenceGate(gl.Contract):
    corroborate_address: Address
    executions: TreeMap[str, ExecutionReceipt]
    execution_count: u256

    def __init__(self, corroborate_address: Address):
        self.corroborate_address = corroborate_address
        self.execution_count = u256(0)

    def _digest(self, value: str, field: str) -> str:
        text = str(value).strip().lower()
        if len(text) != 64 or any(c not in "0123456789abcdef" for c in text):
            raise gl.vm.UserError(f"EXPECTED: {field} must be 32-byte lowercase hex without 0x")
        return text

    @gl.public.write
    def execute_if_corroborated(
        self,
        case_id: u256,
        required_side: u8,
        expected_definition_hash: str,
        expected_finalization_hash: str,
        action_hash: str,
        payload_hash: str,
    ) -> None:
        side = int(required_side)
        if side not in (STANCE_SUPPORTS, STANCE_CONTRADICTS):
            raise gl.vm.UserError("EXPECTED: required_side must be SUPPORTS or CONTRADICTS")
        definition_hash = self._digest(expected_definition_hash, "expected_definition_hash")
        finalization_hash = self._digest(expected_finalization_hash, "expected_finalization_hash")
        action = self._digest(action_hash, "action_hash")
        payload = self._digest(payload_hash, "payload_hash")
        if self.executions.get(action) is not None:
            raise gl.vm.UserError("EXPECTED: protected action was already executed")

        corroborate = ICorroborate(self.corroborate_address)
        if not corroborate.view().is_corroborated(
            case_id,
            definition_hash,
            finalization_hash,
            u8(side),
        ):
            raise gl.vm.UserError("EXPECTED: pinned Corroborate result does not authorize this action")

        self.executions[action] = ExecutionReceipt(
            caller=gl.message.sender_address,
            case_id=case_id,
            required_side=u8(side),
            definition_hash=definition_hash,
            finalization_hash=finalization_hash,
            action_hash=action,
            payload_hash=payload,
        )
        self.execution_count = u256(int(self.execution_count) + 1)

    @gl.public.view
    def was_executed(self, action_hash: str) -> bool:
        return self.executions.get(str(action_hash).strip().lower()) is not None

    @gl.public.view
    def get_execution(self, action_hash: str) -> dict:
        receipt = self.executions.get(str(action_hash).strip().lower())
        if receipt is None:
            return {}
        return {
            "caller": str(receipt.caller),
            "case_id": int(receipt.case_id),
            "required_side": int(receipt.required_side),
            "definition_hash": receipt.definition_hash,
            "finalization_hash": receipt.finalization_hash,
            "action_hash": receipt.action_hash,
            "payload_hash": receipt.payload_hash,
        }
