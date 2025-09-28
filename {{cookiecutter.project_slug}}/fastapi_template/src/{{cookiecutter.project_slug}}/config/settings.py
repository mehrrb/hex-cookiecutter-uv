"""
FastAPI application settings for {{cookiecutter.project_name}}.
"""
from pydantic_settings import BaseSettings
from typing import List
{%- if cookiecutter.db_type == "postgresql" %}
import os
{%- endif %}


class Settings(BaseSettings):
    """Application settings."""
    
    # Application
    DEBUG: bool = False
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    VERSION: str = "1.0.0"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # Database Configuration
    {%- if cookiecutter.db_type == "postgresql" %}
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/{{cookiecutter.project_slug}}"
    {%- elif cookiecutter.db_type == "sqlite" %}
    DATABASE_URL: str = "sqlite:///./{{cookiecutter.project_slug}}.db"
    {%- elif cookiecutter.db_type == "mysql" %}
    DATABASE_URL: str = "mysql://user:password@localhost:3306/{{cookiecutter.project_slug}}"
    {%- endif %}
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
