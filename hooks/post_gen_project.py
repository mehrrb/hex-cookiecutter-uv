#!/usr/bin/env python3
"""
Post-generation hook for {{cookiecutter.project_name}}.

This hook cleans up the generated project by:
1. Moving the selected framework's files to the root
2. Removing the unused framework's files
3. Cleaning up the template structure
4. Handling database-specific configurations
"""

import os
import shutil
import sys
from pathlib import Path


def main():
    """Main post-generation logic."""
    # Get the project directory (where cookiecutter generated the project)
    project_dir = Path.cwd()
    
    # Get the selected framework from the framework selection file
    framework_file = project_dir / 'framework_selection.txt'
    if framework_file.exists():
        framework = framework_file.read_text().strip()
        print(f"Framework selection from file: {framework}")
    else:
        print("No framework selection file found!")
        return
    
    print(f"Setting up {framework} project...")
    
    # Get the template directory (parent of current project)
    template_dir = project_dir.parent / '{{cookiecutter.project_slug}}'
    
    # Define source and target directories
    if framework == 'fastapi':
        source_dir = template_dir / 'fastapi_template'
        remove_dir = template_dir / 'drf_template'
    elif framework == 'django':
        source_dir = template_dir / 'drf_template'
        remove_dir = template_dir / 'fastapi_template'
    else:
        print(f"Unknown framework: {framework}")
        sys.exit(1)
    
    # Handle database-specific configurations
    handle_database_config(project_dir, "{{ cookiecutter.db_type }}")
    
    # Copy the selected framework's files to the project directory
    if source_dir.exists():
        print(f"Copying {framework} files to project...")
        
        # Copy all files from the framework template to project directory
        for item in source_dir.iterdir():
            if item.is_dir():
                if (project_dir / item.name).exists():
                    shutil.rmtree(project_dir / item.name)
                shutil.copytree(str(item), str(project_dir / item.name))
            else:
                shutil.copy2(str(item), str(project_dir / item.name))
    
    # Remove framework selection file
    if framework_file.exists():
        framework_file.unlink()
    
    # Remove template directories from the generated project
    for template_dir in ['fastapi_template', 'drf_template']:
        template_path = project_dir / template_dir
        if template_path.exists():
            print(f"Removing {template_dir} directory...")
            shutil.rmtree(template_path)
    
    # Remove placeholder files
    for placeholder in ['PLACEHOLDER_FASTAPI', 'PLACEHOLDER_DJANGO']:
        placeholder_path = project_dir / placeholder
        if placeholder_path.exists():
            placeholder_path.unlink()
    
    print(f"✅ {framework.title()} project setup complete!")
    print(f"📁 Project structure ready in {project_dir}")
    
    # Print next steps
    if framework == 'fastapi':
        print("\n🚀 Next steps:")
        print("1. cd into your project directory")
        print("2. Install dependencies: uv sync")
        print("3. Run the application: python -m src.{{cookiecutter.project_slug}}.main")
        print("4. Visit http://localhost:8000/docs for API documentation")
    else:  # django
        print("\n🚀 Next steps:")
        print("1. cd into your project directory")
        print("2. Install dependencies: uv sync")
        print("3. Run migrations: python src/{{cookiecutter.project_slug}}/manage.py migrate")
        print("4. Start the development server: python src/{{cookiecutter.project_slug}}/manage.py runserver")
        print("5. Visit http://localhost:8000 for your Django application")


def handle_database_config(project_dir: Path, db_type: str):
    """Handle database-specific configurations."""
    print(f"🔧 Configuring database for {db_type}...")
    
    if db_type == "sqlite":
        # SQLite doesn't need additional database service in docker-compose
        print("SQLite selected - no additional database service needed")
    elif db_type == "postgresql":
        print("PostgreSQL selected - database service will be included")
    elif db_type == "mysql":
        print("MySQL selected - database service will be included")
    
    # Create .env file with database-specific settings
    env_file = project_dir / ".env"
    env_content = f"""# Database Configuration
DATABASE_URL={db_type}://user:password@localhost:5432/{{cookiecutter.project_slug}}

# Application Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
"""
    
    if db_type == "sqlite":
        env_content = f"""# Database Configuration
DATABASE_URL=sqlite:///./{{cookiecutter.project_slug}}.db

# Application Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
"""
    elif db_type == "mysql":
        env_content = f"""# Database Configuration
DATABASE_URL=mysql://user:password@localhost:3306/{{cookiecutter.project_slug}}

# Application Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
"""
    
    env_file.write_text(env_content)
    print(f"Created .env file with {db_type} configuration")


if __name__ == '__main__':
    main()
