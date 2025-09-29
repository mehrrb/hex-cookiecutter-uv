"""
User service for {{cookiecutter.project_name}}.
"""
from typing import List, Optional
from uuid import UUID

from {{cookiecutter.project_slug}}.domain.entities.user import User  # type: ignore


class UserService:
    """User domain service."""

    def __init__(self, user_repository):
        """Initialize user service with repository."""
        self.user_repository = user_repository

    async def create_user(self, email: str, name: str) -> User:
        """Create a new user."""
        # Check if user already exists
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError(f"User with email {email} already exists")

        # Create new user
        user = User.create(email=email, name=name)

        # Save to repository
        await self.user_repository.save(user)

        return user

    async def get_user(self, user_id: UUID) -> Optional[User]:
        """Get user by ID."""
        return await self.user_repository.get_by_id(user_id)

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return await self.user_repository.get_by_email(email)

    async def get_all_users(self) -> List[User]:
        """Get all users."""
        return await self.user_repository.get_all()

    async def update_user_name(self, user_id: UUID, name: str) -> Optional[User]:
        """Update user name."""
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            return None

        user.update_name(name)
        await self.user_repository.save(user)

        return user

    async def deactivate_user(self, user_id: UUID) -> Optional[User]:
        """Deactivate user."""
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            return None

        user.deactivate()
        await self.user_repository.save(user)

        return user

    async def activate_user(self, user_id: UUID) -> Optional[User]:
        """Activate user."""
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            return None

        user.activate()
        await self.user_repository.save(user)

        return user
