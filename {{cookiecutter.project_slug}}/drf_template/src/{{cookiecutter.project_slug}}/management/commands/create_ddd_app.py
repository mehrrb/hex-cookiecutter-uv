#!/usr/bin/env python3
"""
Custom Django management command to create DDD-structured apps.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = 'Create a new Django app with DDD (Domain-Driven Design) structure'

    def add_arguments(self, parser):
        parser.add_argument(
            'app_name',
            type=str,
            help='Name of the app to create'
        )
        parser.add_argument(
            '--service-name',
            type=str,
            help='Service name for DDD structure (defaults to app_name)'
        )

    def handle(self, *args, **options):
        app_name = options['app_name']
        service_name = options.get('service_name') or app_name

        # Validate app name
        if not app_name.isidentifier():
            raise CommandError(f"'{app_name}' is not a valid app name. App names must be valid Python identifiers.")

        self.stdout.write(f"Creating DDD app: {app_name}")
        self.stdout.write(f"Service name: {service_name}")

        # Get the project root (src directory)
        project_root = Path(settings.BASE_DIR)
        # Go to src directory (project_root is {{cookiecutter.project_slug}}, we need src/{{cookiecutter.project_slug}})
        src_dir = project_root / "src"

        # Create service directory structure inside src/
        service_dir = src_dir / f"{service_name}_service"

        if service_dir.exists():
            raise CommandError(f"Service directory '{service_dir}' already exists!")

        # Create DDD directory structure
        self.create_ddd_structure(service_dir, app_name)

        # Create Django app in infrastructure layer
        self.create_django_app(service_dir, app_name)

        # Move Django app files to infrastructure
        self.move_django_app_to_infrastructure(service_dir, app_name)

        # Create domain layer files
        self.create_domain_layer(service_dir, app_name)

        # Create application layer files
        self.create_application_layer(service_dir, app_name)

        # Create presentation layer files
        self.create_presentation_layer(service_dir, app_name)

        # Update Django settings
        self.update_django_settings(app_name)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created DDD app '{app_name}' with service '{service_name}'"
            )
        )
        self.stdout.write(f"Service structure created at: {service_dir}")
        self.stdout.write("\nNext steps:")
        self.stdout.write(f"1. Run migrations: python manage.py makemigrations {app_name}")
        self.stdout.write(f"2. Apply migrations: python manage.py migrate")
        self.stdout.write(f"3. Update your domain logic in {service_dir}/domain/")
        self.stdout.write(f"4. Update your application services in {service_dir}/application/")

    def create_ddd_structure(self, service_dir, app_name):
        """Create the basic DDD directory structure."""
        directories = [
            service_dir,
            service_dir / "domain",
            service_dir / "domain" / "entities",
            service_dir / "domain" / "services",
            service_dir / "domain" / "repositories",
            service_dir / "application",
            service_dir / "application" / "services",
            service_dir / "application" / "dto",
            service_dir / "infrastructure",
            service_dir / "presentation",
            service_dir / "presentation" / "api",
            service_dir / "presentation" / "serializers",
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            # Create __init__.py files
            (directory / "__init__.py").touch()

        self.stdout.write(f"Created DDD structure for {app_name}")

    def create_django_app(self, service_dir, app_name):
        """Create Django app using startapp command."""
        infrastructure_dir = service_dir / "infrastructure"

        # Change to infrastructure directory and run startapp
        original_cwd = os.getcwd()
        try:
            os.chdir(infrastructure_dir)
            call_command('startapp', app_name)
            self.stdout.write(f"Created Django app '{app_name}' in infrastructure")
        finally:
            os.chdir(original_cwd)

    def move_django_app_to_infrastructure(self, service_dir, app_name):
        """Move Django app files to proper infrastructure structure."""
        infrastructure_dir = service_dir / "infrastructure"
        app_dir = infrastructure_dir / app_name

        if not app_dir.exists():
            raise CommandError(f"Django app directory '{app_dir}' not found!")

        # Create additional infrastructure directories
        infrastructure_subdirs = [
            "repositories",
            "external_services",
            "persistence",
        ]

        for subdir in infrastructure_subdirs:
            (infrastructure_dir / subdir).mkdir(exist_ok=True)
            (infrastructure_dir / subdir / "__init__.py").touch()

        self.stdout.write(f"Moved Django app to infrastructure layer")

    def create_domain_layer(self, service_dir, app_name):
        """Create domain layer files."""
        domain_dir = service_dir / "domain"

        # Create empty entity file
        entity_file = domain_dir / "entities" / f"{app_name}.py"
        entity_file.write_text("")

        # Create empty repository file
        repository_file = domain_dir / "repositories" / f"{app_name}_repository.py"
        repository_file.write_text("")

        # Create empty domain service file
        service_file = domain_dir / "services" / f"{app_name}_service.py"
        service_file.write_text("")

        self.stdout.write(f"Created domain layer files for {app_name}")

    def create_application_layer(self, service_dir, app_name):
        """Create application layer files."""
        application_dir = service_dir / "application"

        # Create empty DTO file
        dto_file = application_dir / "dto" / f"{app_name}_dto.py"
        dto_file.write_text("")

        # Create empty application service file
        app_service_file = application_dir / "services" / f"{app_name}_application_service.py"
        app_service_file.write_text("")

        self.stdout.write(f"Created application layer files for {app_name}")

    def create_presentation_layer(self, service_dir, app_name):
        """Create presentation layer files."""
        presentation_dir = service_dir / "presentation"

        # Create empty serializer file
        serializer_file = presentation_dir / "serializers" / f"{app_name}_serializer.py"
        serializer_file.write_text("")

        # Create empty API views file
        api_file = presentation_dir / "api" / f"{app_name}_views.py"
        api_file.write_text("")

        # Create empty URLs file
        urls_file = presentation_dir / "api" / f"{app_name}_urls.py"
        urls_file.write_text("")

        self.stdout.write(f"Created presentation layer files for {app_name}")

    def update_django_settings(self, app_name):
        """Add the new app to Django settings."""
        # This would require modifying settings.py
        # For now, just inform the user
        self.stdout.write(f"Remember to add '{app_name}' to INSTALLED_APPS in settings.py")
