"""
Dependency injection container for {{cookiecutter.project_name}}.
"""
from {{cookiecutter.project_slug}}.adapters.driven.external.email_adapter import EmailAdapter
from {{cookiecutter.project_slug}}.adapters.driven.persistence.user_repository import DjangoUserRepository
from {{cookiecutter.project_slug}}.domain.services.user_service import UserService


class Container:
    """Dependency injection container."""
    
    def __init__(self):
        """Initialize container with dependencies."""
        # Initialize repositories
        self.user_repository = DjangoUserRepository()
        
        # Initialize external services
        self.email_adapter = EmailAdapter()
        
        # Initialize domain services
        self.user_service = UserService(self.user_repository)
    
    def get_user_service(self) -> UserService:
        """Get user service instance."""
        return self.user_service
    
    def get_email_adapter(self) -> EmailAdapter:
        """Get email adapter instance."""
        return self.email_adapter
