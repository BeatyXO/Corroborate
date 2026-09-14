import os
import tempfile

import pytest


def _windows_safe_inject_message_to_fd0(vm):
    """Compatibility shim for genlayer-test 0.29.2 on Windows.

    The pinned loader unlinks the temporary stdin file while fd 0 still
    references it. Windows rejects that unlink; the file is intentionally
    retained until the process exits, matching the loader's effective Unix
    semantics without changing contract execution.
    """
    from genlayer.py import calldata
    from genlayer.py.types import Address

    def address(value):
        return Address(value) if isinstance(value, bytes) else value

    message_data = {
        "contract_address": address(vm._contract_address),
        "sender_address": address(vm.sender),
        "origin_address": address(vm.origin),
        "stack": [],
        "value": vm._value,
        "datetime": vm._datetime,
        "is_init": False,
        "chain_id": vm._chain_id,
        "entry_kind": 0,
        "entry_data": b"",
        "entry_stage_data": None,
    }
    fd, _path = tempfile.mkstemp()
    os.write(fd, calldata.encode(message_data))
    os.lseek(fd, 0, os.SEEK_SET)
    vm._original_stdin_fd = os.dup(0)
    os.dup2(fd, 0)
    os.close(fd)


try:
    import gltest.direct.loader as _loader
    _loader._inject_message_to_fd0 = _windows_safe_inject_message_to_fd0
except ImportError:
    pass

@pytest.fixture(autouse=True)
def _reset_contract_registry():
    yield
    try:
        import genlayer.gl.genvm_contracts as contracts
    except ImportError:
        return
    contracts.__known_contract__ = None
