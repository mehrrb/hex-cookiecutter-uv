"""
Email adapter for {{cookiecutter.project_name}}.
"""
from typing import Dict, Any


class EmailAdapter:
    """Email service adapter."""
    
    async def send_welcome_email(self, email: str, name: str) -> bool:
        """Send welcome email to new user."""
        # TODO: Implement email sending logic
        # For now, just log the action
        print(f"Sending welcome email to {name} ({email})")
        return True
    
    async def send_password_reset_email(self, email: str, reset_token: str) -> bool:
        """Send password reset email."""
        # TODO: Implement password reset email logic
        print(f"Sending password reset email to {email} with token {reset_token}")
        return True
    
    async def send_notification_email(self, email: str, subject: str, message: str) -> bool:
        """Send notification email."""
        # TODO: Implement notification email logic
        print(f"Sending notification email to {email}: {subject}")
        return True
