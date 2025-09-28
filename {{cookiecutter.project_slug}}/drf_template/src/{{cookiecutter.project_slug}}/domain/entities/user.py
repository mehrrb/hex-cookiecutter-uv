"""
User entity for {{cookiecutter.project_name}}.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class User:
    """User domain entity."""
    
    id: UUID
    email: str
    name: str
    is_active: bool = True
    created_at: datetime = None
    updated_at: datetime = None
    
    def __post_init__(self):
        """Initialize default values after object creation."""
        if self.created_at is None:
            self.created_at = datetime.utcnow()
        if self.updated_at is None:
            self.updated_at = datetime.utcnow()
    
    def update_name(self, name: str) -> None:
        """Update user name."""
        self.name = name
        self.updated_at = datetime.utcnow()
    
    def deactivate(self) -> None:
        """Deactivate user."""
        self.is_active = False
        self.updated_at = datetime.utcnow()
    
    def activate(self) -> None:
        """Activate user."""
        self.is_active = True
        self.updated_at = datetime.utcnow()
    
    @classmethod
    def create(cls, email: str, name: str) -> "User":
        """Create a new user."""
        return cls(
            id=uuid4(),
            email=email,
            name=name,
            is_active=True
        )
