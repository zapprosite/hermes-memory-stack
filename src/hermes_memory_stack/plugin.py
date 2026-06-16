"""MemoryStackPlugin: hermes-memory-stack para hermes-agent."""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger("hermes-memory-stack")


class MemoryStackPlugin:
    """Plugin exclusive."""
    name = "hermes-memory-stack"
    kind = "exclusive"
    version = "1.0.0"

    def register(self, ctx) -> None:
        """Hook de registro."""
        # Tools
        ctx.register_tool("hermes_memory_stack_status", self._tool_status)

        # Skills
        skill_path = self._skill_path()
        if skill_path.exists():
            ctx.register_skill("hermes-memory-stack", skill_path)

        log.info("hermes-memory-stack v%s registrado", self.version)

    def _skill_path(self) -> Path:
        return Path(__file__).parent.parent.parent / "skills" / "memory-stack"

    def _tool_status(self, **_):
        return {"status": "ready", "version": self.version}
