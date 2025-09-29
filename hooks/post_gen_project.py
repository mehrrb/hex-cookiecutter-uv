#!/usr/bin/env python3
"""
Post-generation hook for {{cookiecutter.project_name}}.
"""

import shutil
import sys
from pathlib import Path


def main():
    project_dir = Path.cwd()
    project_slug = project_dir.name
    framework_file = project_dir / "framework_selection.txt"
    if framework_file.exists():
        framework = framework_file.read_text().strip()
        print(f"Framework selection from file: {framework}")
    else:
        print("No framework selection file found!")
        return

    print(f"Setting up {framework} project...")

    template_dir = project_dir.parent / "{{cookiecutter.project_slug}}"

    if framework == "fastapi":
        source_dir = template_dir / "fastapi_template"
        remove_dir = template_dir / "drf_template"
        print(f"Removing {remove_dir} directory...")
    elif framework == "drf":
        source_dir = template_dir / "drf_template"
        remove_dir = template_dir / "fastapi_template"
        print(f"Removing {remove_dir} directory...")
    else:
        print(f"Unknown framework: {framework}")
        sys.exit(1)

    if framework == "drf":
        handle_database_config(project_dir, "postgresql")
    else:
        handle_database_config(project_dir, "{{ cookiecutter.db_type }}")

    if source_dir.exists():
        print(f"Copying {framework} files to project...")
        for item in source_dir.iterdir():
            if item.is_dir():
                if (project_dir / item.name).exists():
                    shutil.rmtree(project_dir / item.name)
                shutil.copytree(str(item), str(project_dir / item.name))
            else:
                shutil.copy2(str(item), str(project_dir / item.name))

    if framework_file.exists():
        framework_file.unlink()

    for template_dir in ["fastapi_template", "drf_template"]:
        template_path = project_dir / template_dir
        if template_path.exists():
            print(f"Removing {template_dir} directory...")
            shutil.rmtree(template_path)

    for placeholder in ["PLACEHOLDER_FASTAPI", "PLACEHOLDER_DRF"]:
        placeholder_path = project_dir / placeholder
        if placeholder_path.exists():
            placeholder_path.unlink()

    print(f"{framework.upper()} project setup complete!")
    print(f"Project structure ready in {project_dir}")

    if framework == "fastapi":
        print("\nNext steps:")
        print("1. cd into your project directory")
        print("2. Install dependencies: uv sync")
        print(f"3. Run the application: python -m src.{project_slug}.main")
        print("4. Visit http://localhost:8000/docs for API documentation")
    else:
        print("\nNext steps:")
        print("1. cd into your project directory")
        print("2. Install dependencies: uv sync")
        print(f"3. Run migrations: python src/{project_slug}/manage.py migrate")
        print(
            f"4. Start the development server: python src/{project_slug}/manage.py runserver"
        )
        print("5. Visit http://localhost:8000 for your DRF application")


def handle_database_config(project_dir: Path, db_type: str):
    print(f"Configuring database for {db_type}...")

    if db_type == "sqlite":
        print("SQLite selected - no additional database service needed")
    elif db_type == "postgresql":
        print("PostgreSQL selected - database service will be included")

    env_file = project_dir / ".env"

    if db_type == "sqlite":
        env_content = """# Database Configuration
DATABASE_URL=sqlite:///./{{cookiecutter.project_slug}}.db

# Application Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
"""
    elif db_type == "postgresql":
        env_content = """# Database Configuration
DB_NAME={{cookiecutter.project_slug}}
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# Application Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
"""

    env_file.write_text(env_content)
    print(f"Created .env file with {db_type} configuration")


if __name__ == "__main__":
    main()
