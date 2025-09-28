#!/usr/bin/env python3
"""
Test script for cookiecutter hooks functionality.
Tests the post-generation hook behavior.
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path


def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            cwd=cwd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout, e.stderr


def test_hook_fastapi_cleanup():
    """Test that hook properly cleans up FastAPI project."""
    print("🧪 Testing FastAPI hook cleanup...")
    
    # Clean up any existing test project
    if os.path.exists("test-hook-fastapi"):
        shutil.rmtree("test-hook-fastapi")
    
    # Generate FastAPI project
    cmd = """cookiecutter . --no-input \
        project_name="Hook FastAPI" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook FastAPI test" \
        db_type="sqlite" """
    
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"❌ FastAPI generation failed: {stderr}")
        return False
    
    # Check that project was created
    if not os.path.exists("hook-fastapi"):
        print("❌ FastAPI project directory not created")
        return False
    
    # Check that template directories are removed
    template_dirs = ["fastapi_template", "drf_template"]
    for template_dir in template_dirs:
        template_path = f"hook-fastapi/{template_dir}"
        if os.path.exists(template_path):
            print(f"❌ Template directory {template_dir} should be removed")
            return False
    
    # Check that placeholder files are removed
    placeholder_files = ["PLACEHOLDER_FASTAPI", "PLACEHOLDER_DRF"]
    for placeholder in placeholder_files:
        placeholder_path = f"hook-fastapi/{placeholder}"
        if os.path.exists(placeholder_path):
            print(f"❌ Placeholder file {placeholder} should be removed")
            return False
    
    # Check that framework selection file is removed
    framework_file = "hook-fastapi/framework_selection.txt"
    if os.path.exists(framework_file):
        print("❌ Framework selection file should be removed")
        return False
    
    # Check that .env file is created
    env_file = "hook-fastapi/.env"
    if not os.path.exists(env_file):
        print("❌ .env file should be created")
        return False
    
    # Check .env content for SQLite
    with open(env_file, 'r') as f:
        content = f.read()
        if "sqlite" not in content:
            print("❌ .env file should contain SQLite configuration")
            return False
    
    print("✅ FastAPI hook cleanup test passed!")
    return True


def test_hook_drf_cleanup():
    """Test that hook properly cleans up DRF project."""
    print("🧪 Testing DRF hook cleanup...")
    
    # Clean up any existing test project
    if os.path.exists("test-hook-drf"):
        shutil.rmtree("test-hook-drf")
    
    # Generate DRF project
    cmd = """cookiecutter . --no-input \
        project_name="Hook DRF" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook DRF test" \
        db_type="postgresql" """
    
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"❌ DRF generation failed: {stderr}")
        return False
    
    # Check that project was created
    if not os.path.exists("hook-drf"):
        print("❌ DRF project directory not created")
        return False
    
    # Check that template directories are removed
    template_dirs = ["fastapi_template", "drf_template"]
    for template_dir in template_dirs:
        template_path = f"hook-drf/{template_dir}"
        if os.path.exists(template_path):
            print(f"❌ Template directory {template_dir} should be removed")
            return False
    
    # Check that placeholder files are removed
    placeholder_files = ["PLACEHOLDER_FASTAPI", "PLACEHOLDER_DRF"]
    for placeholder in placeholder_files:
        placeholder_path = f"hook-drf/{placeholder}"
        if os.path.exists(placeholder_path):
            print(f"❌ Placeholder file {placeholder} should be removed")
            return False
    
    # Check that framework selection file is removed
    framework_file = "hook-drf/framework_selection.txt"
    if os.path.exists(framework_file):
        print("❌ Framework selection file should be removed")
        return False
    
    # Check that .env file is created
    env_file = "hook-drf/.env"
    if not os.path.exists(env_file):
        print("❌ .env file should be created")
        return False
    
    # Check .env content for PostgreSQL
    with open(env_file, 'r') as f:
        content = f.read()
        if "postgresql" not in content:
            print("❌ .env file should contain PostgreSQL configuration")
            return False
    
    print("✅ DRF hook cleanup test passed!")
    return True


def test_hook_database_config():
    """Test database configuration in .env files."""
    print("🧪 Testing database configuration...")
    
    # Test SQLite configuration
    if os.path.exists("test-hook-sqlite"):
        shutil.rmtree("test-hook-sqlite")
    
    cmd = """cookiecutter . --no-input \
        project_name="Hook SQLite" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook SQLite test" \
        db_type="sqlite" """
    
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"❌ SQLite generation failed: {stderr}")
        return False
    
    # Check SQLite .env content
    env_file = "hook-sqlite/.env"
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            content = f.read()
            if "sqlite:///./hook-sqlite.db" not in content:
                print("❌ SQLite .env file should contain correct database URL")
                return False
    
    # Test PostgreSQL configuration
    if os.path.exists("test-hook-postgresql"):
        shutil.rmtree("test-hook-postgresql")
    
    cmd = """cookiecutter . --no-input \
        project_name="Hook PostgreSQL" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook PostgreSQL test" \
        db_type="postgresql" """
    
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"❌ PostgreSQL generation failed: {stderr}")
        return False
    
    # Check PostgreSQL .env content
    env_file = "hook-postgresql/.env"
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            content = f.read()
            if "postgresql://user:password@localhost:5432/hook-postgresql" not in content:
                print("❌ PostgreSQL .env file should contain correct database URL")
                return False
    
    print("✅ Database configuration test passed!")
    return True


def test_hook_next_steps():
    """Test that next steps are printed correctly."""
    print("🧪 Testing next steps output...")
    
    # Test FastAPI next steps
    if os.path.exists("test-hook-steps-fastapi"):
        shutil.rmtree("test-hook-steps-fastapi")
    
    cmd = """cookiecutter . --no-input \
        project_name="Hook Steps FastAPI" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook steps FastAPI test" \
        db_type="sqlite" """
    
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"❌ FastAPI generation failed: {stderr}")
        return False
    
    # Check that FastAPI project has correct structure
    expected_files = [
        "hook-steps-fastapi/src/hook-steps-fastapi/main.py",
        "hook-steps-fastapi/pyproject.toml",
        "hook-steps-fastapi/Dockerfile",
    ]
    
    for file_path in expected_files:
        if not os.path.exists(file_path):
            print(f"❌ Missing FastAPI file: {file_path}")
            return False
    
    # Test DRF next steps
    if os.path.exists("test-hook-steps-drf"):
        shutil.rmtree("test-hook-steps-drf")
    
    cmd = """cookiecutter . --no-input \
        project_name="Hook Steps DRF" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook steps DRF test" \
        db_type="sqlite" """
    
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"❌ DRF generation failed: {stderr}")
        return False
    
    # Check that DRF project has correct structure
    expected_files = [
        "hook-steps-drf/src/hook-steps-drf/manage.py",
        "hook-steps-drf/src/hook-steps-drf/wsgi.py",
        "hook-steps-drf/src/hook-steps-drf/config/settings.py",
        "hook-steps-drf/pyproject.toml",
        "hook-steps-drf/Dockerfile",
    ]
    
    for file_path in expected_files:
        if not os.path.exists(file_path):
            print(f"❌ Missing DRF file: {file_path}")
            return False
    
    print("✅ Next steps test passed!")
    return True


def cleanup():
    """Clean up test projects."""
    print("🧹 Cleaning up test projects...")
    
    test_projects = [
        "hook-fastapi",
        "hook-drf",
        "hook-sqlite",
        "hook-postgresql",
        "hook-steps-fastapi",
        "hook-steps-drf",
    ]
    
    for project in test_projects:
        if os.path.exists(project):
            shutil.rmtree(project)
            print(f"  🗑️  Removed {project}")


def main():
    """Run all hook tests."""
    print("🚀 Starting cookiecutter hooks tests...")
    print("=" * 50)
    
    tests = [
        test_hook_fastapi_cleanup,
        test_hook_drf_cleanup,
        test_hook_database_config,
        test_hook_next_steps,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with exception: {e}")
            failed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All hook tests passed!")
        return 0
    else:
        print("💥 Some hook tests failed!")
        return 1


if __name__ == "__main__":
    try:
        exit_code = main()
    finally:
        cleanup()
    sys.exit(exit_code)
