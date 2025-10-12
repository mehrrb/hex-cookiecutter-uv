"""
User entity for {{cookiecutter.project_name}}.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class User:
    """User domain entity."""

    id: UUID
    email: str
    name: str
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        """Initialize default values after object creation."""
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)
        if self.updated_at is None:
            self.updated_at = datetime.now(timezone.utc)

    def update_name(self, name: str) -> None:
        """Update user name."""
        self.name = name
        self.updated_at = datetime.now(timezone.utc)

    def deactivate(self) -> None:
        """Deactivate user."""
        self.is_active = False
        self.updated_at = datetime.now(timezone.utc)

    def activate(self) -> None:
        """Activate user."""
        self.is_active = True
        self.updated_at = datetime.now(timezone.utc)

    @classmethod
    def create(cls, email: str, name: str) -> "User":
        """Create a new user."""
        return cls(id=uuid4(), email=email, name=name, is_active=True)
