#!/usr/bin/env python3

import os
import shutil
import subprocess

import pytest


def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    try:
        env = os.environ.copy()
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True,
            env=env,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout, e.stderr


@pytest.fixture(autouse=True)
def cleanup_after_test():
    """Clean up test projects after each test."""
    yield
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


def test_hook_fastapi_cleanup():
    """Test that hook properly cleans up FastAPI project."""
    if os.path.exists("test-hook-fastapi"):
        shutil.rmtree("test-hook-fastapi")

    cmd = """cookiecutter . --no-input \
        project_name="Hook FastAPI" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook FastAPI test" \
        db_type="sqlite" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"FastAPI generation failed: {stderr}"
    assert os.path.exists("hook-fastapi"), "FastAPI project directory not created"

    template_dirs = ["fastapi_template", "drf_template"]
    for template_dir in template_dirs:
        template_path = f"hook-fastapi/{template_dir}"
        assert not os.path.exists(
            template_path
        ), f"Template directory {template_dir} should be removed"

    placeholder_files = ["PLACEHOLDER_FASTAPI", "PLACEHOLDER_DRF"]
    for placeholder in placeholder_files:
        placeholder_path = f"hook-fastapi/{placeholder}"
        assert not os.path.exists(
            placeholder_path
        ), f"Placeholder file {placeholder} should be removed"

    framework_file = "hook-fastapi/framework_selection.txt"
    assert not os.path.exists(
        framework_file
    ), "Framework selection file should be removed"

    env_file = "hook-fastapi/.env"
    assert os.path.exists(env_file), ".env file should be created"

    with open(env_file, "r") as f:
        content = f.read()
        assert "sqlite" in content, ".env file should contain SQLite configuration"


def test_hook_drf_cleanup():
    """Test that hook properly cleans up DRF project."""
    if os.path.exists("test-hook-drf"):
        shutil.rmtree("test-hook-drf")

    cmd = """cookiecutter . --no-input \
        project_name="Hook DRF" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook DRF test" \
        db_type="postgresql" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"DRF generation failed: {stderr}"
    assert os.path.exists("hook-drf"), "DRF project directory not created"

    template_dirs = ["fastapi_template", "drf_template"]
    for template_dir in template_dirs:
        template_path = f"hook-drf/{template_dir}"
        assert not os.path.exists(
            template_path
        ), f"Template directory {template_dir} should be removed"

    placeholder_files = ["PLACEHOLDER_FASTAPI", "PLACEHOLDER_DRF"]
    for placeholder in placeholder_files:
        placeholder_path = f"hook-drf/{placeholder}"
        assert not os.path.exists(
            placeholder_path
        ), f"Placeholder file {placeholder} should be removed"

    framework_file = "hook-drf/framework_selection.txt"
    assert not os.path.exists(
        framework_file
    ), "Framework selection file should be removed"

    env_file = "hook-drf/.env"
    assert os.path.exists(env_file), ".env file should be created"

    with open(env_file, "r") as f:
        content = f.read()
        assert (
            "DB_NAME=hook-drf" in content
        ), ".env file should contain PostgreSQL configuration"


def test_hook_database_config():
    """Test database configuration in .env files."""
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
    assert returncode == 0, f"SQLite generation failed: {stderr}"

    env_file = "hook-sqlite/.env"
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            content = f.read()
            assert (
                "DATABASE_URL=sqlite:///./hook-sqlite.db" in content
            ), "SQLite .env file should contain correct database URL"

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
    assert returncode == 0, f"PostgreSQL generation failed: {stderr}"

    env_file = "hook-postgresql/.env"
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            content = f.read()
            assert (
                "DB_NAME=hook-postgresql" in content
            ), "PostgreSQL .env file should contain correct database URL"


def test_hook_next_steps():
    """Test that next steps are printed correctly."""
    if os.path.exists("test-hook-steps-fastapi"):
        shutil.rmtree("test-hook-steps-fastapi")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "fastapi"

    cmd = """cookiecutter . --no-input \
        project_name="Hook Steps FastAPI" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook steps FastAPI test" \
        db_type="sqlite" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"FastAPI generation failed: {stderr}"

    expected_files = [
        "hook-steps-fastapi/src/hook-steps-fastapi/main.py",
        "hook-steps-fastapi/pyproject.toml",
        "hook-steps-fastapi/Dockerfile",
    ]

    for file_path in expected_files:
        assert os.path.exists(file_path), f"Missing FastAPI file: {file_path}"

    if os.path.exists("test-hook-steps-drf"):
        shutil.rmtree("test-hook-steps-drf")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "drf"

    cmd = """cookiecutter . --no-input \
        project_name="Hook Steps DRF" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="Hook steps DRF test" \
        db_type="sqlite" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"DRF generation failed: {stderr}"

    expected_files = [
        "hook-steps-drf/src/hook-steps-drf/manage.py",
        "hook-steps-drf/src/hook-steps-drf/wsgi.py",
        "hook-steps-drf/src/hook-steps-drf/config/settings.py",
        "hook-steps-drf/pyproject.toml",
        "hook-steps-drf/Dockerfile",
    ]

    for file_path in expected_files:
        assert os.path.exists(file_path), f"Missing DRF file: {file_path}"
