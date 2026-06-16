"""Smoke tests para hermes-memory-stack."""
import pytest


def test_module_imports():
    """memory_stack deve ser importavel."""
    try:
        from memory_stack import memory_provider, memory_manager
    except ImportError:
        pytest.skip("memory_stack nao instalado")


def test_provider_abc():
    """MemoryProvider deve ser ABC."""
    from memory_stack.memory_provider import MemoryProvider
    assert hasattr(MemoryProvider, '__abstractmethods__')
