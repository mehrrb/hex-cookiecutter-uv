#!/usr/bin/env python3

import os
import shutil
import subprocess

import pytest


def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd, capture_output=True, text=True, check=True
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout, e.stderr


@pytest.fixture(autouse=True)
def cleanup_after_test():
    """Clean up test projects after each test."""
    yield
    test_projects = [
        "test-fastapi-sqlite",
        "test-fastapi-postgresql",
        "test-drf-sqlite",
        "test-drf-postgresql",
        "docker-build",
        "drffunc",
        "debug-drf",
        "debug-test",
    ]
    for project in test_projects:
        if os.path.exists(project):
            shutil.rmtree(project)


def test_fastapi_sqlite():
    """Test FastAPI project generation with SQLite."""
    if os.path.exists("test-fastapi-sqlite"):
        shutil.rmtree("test-fastapi-sqlite")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "fastapi"

    cmd = """cookiecutter . --no-input \
        project_name="Test FastAPI SQLite" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test FastAPI project with SQLite" \
        db_type="sqlite" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"Failed to generate FastAPI SQLite project: {stderr}"
    assert os.path.exists(
        "test-fastapi-sqlite"
    ), "FastAPI SQLite project directory not created"

    expected_files = [
        "test-fastapi-sqlite/pyproject.toml",
        "test-fastapi-sqlite/src/test-fastapi-sqlite/main.py",
        "test-fastapi-sqlite/src/test-fastapi-sqlite/domain/entities/user.py",
        "test-fastapi-sqlite/src/test-fastapi-sqlite/domain/services/user_service.py",
        "test-fastapi-sqlite/Dockerfile",
    ]

    for file_path in expected_files:
        assert os.path.exists(file_path), f"Missing file: {file_path}"

    docker_compose_path = "test-fastapi-sqlite/docker-compose.yml"
    if os.path.exists(docker_compose_path):
        with open(docker_compose_path, "r") as f:
            content = f.read().strip()
            assert (
                not content
            ), f"docker-compose.yml should be empty for SQLite, but contains: {content}"

    returncode, stdout, stderr = run_command("uv sync", cwd="test-fastapi-sqlite")
    assert returncode == 0, f"uv sync failed: {stderr}"


def test_fastapi_postgresql():
    """Test FastAPI project generation with PostgreSQL."""
    if os.path.exists("test-fastapi-postgresql"):
        shutil.rmtree("test-fastapi-postgresql")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "fastapi"

    cmd = """cookiecutter . --no-input \
        project_name="Test FastAPI PostgreSQL" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test FastAPI project with PostgreSQL" \
        db_type="postgresql" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"Failed to generate FastAPI PostgreSQL project: {stderr}"
    assert os.path.exists(
        "test-fastapi-postgresql"
    ), "FastAPI PostgreSQL project directory not created"

    docker_compose_path = "test-fastapi-postgresql/docker-compose.yml"
    assert os.path.exists(
        docker_compose_path
    ), "docker-compose.yml not created for PostgreSQL"

    with open(docker_compose_path, "r") as f:
        content = f.read()
        assert (
            "postgres:15" in content
        ), "PostgreSQL service not found in docker-compose.yml"

    pyproject_path = "test-fastapi-postgresql/pyproject.toml"
    if os.path.exists(pyproject_path):
        with open(pyproject_path, "r") as f:
            content = f.read()
            assert (
                "psycopg2-binary" in content
            ), "psycopg2-binary not found in pyproject.toml"


def test_drf_sqlite():
    """Test DRF project generation with SQLite."""
    if os.path.exists("test-drf-sqlite"):
        shutil.rmtree("test-drf-sqlite")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "drf"

    cmd = """cookiecutter . --no-input \
        project_name="Test DRF SQLite" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test DRF project with SQLite" \
        db_type="sqlite" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"Failed to generate DRF SQLite project: {stderr}"
    assert os.path.exists("test-drf-sqlite"), "DRF SQLite project directory not created"

    expected_files = [
        "test-drf-sqlite/pyproject.toml",
        "test-drf-sqlite/src/test-drf-sqlite/manage.py",
        "test-drf-sqlite/src/test-drf-sqlite/wsgi.py",
        "test-drf-sqlite/src/test-drf-sqlite/config/settings.py",
        "test-drf-sqlite/src/test-drf-sqlite/domain/entities/user.py",
        "test-drf-sqlite/src/test-drf-sqlite/domain/services/user_service.py",
        "test-drf-sqlite/Dockerfile",
    ]

    for file_path in expected_files:
        assert os.path.exists(file_path), f"Missing file: {file_path}"

    docker_compose_path = "test-drf-sqlite/docker-compose.yml"
    if os.path.exists(docker_compose_path):
        with open(docker_compose_path, "r") as f:
            content = f.read().strip()
            assert (
                not content
            ), f"docker-compose.yml should be empty for SQLite, but contains: {content}"

    returncode, stdout, stderr = run_command("uv sync", cwd="test-drf-sqlite")
    assert returncode == 0, f"uv sync failed: {stderr}"


def test_drf_postgresql():
    """Test DRF project generation with PostgreSQL."""
    if os.path.exists("test-drf-postgresql"):
        shutil.rmtree("test-drf-postgresql")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "drf"

    cmd = """cookiecutter . --no-input \
        project_name="Test DRF PostgreSQL" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test DRF project with PostgreSQL" \
        db_type="postgresql" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"Failed to generate DRF PostgreSQL project: {stderr}"
    assert os.path.exists(
        "test-drf-postgresql"
    ), "DRF PostgreSQL project directory not created"

    docker_compose_path = "test-drf-postgresql/docker-compose.yml"
    assert os.path.exists(
        docker_compose_path
    ), "docker-compose.yml not created for PostgreSQL"

    with open(docker_compose_path, "r") as f:
        content = f.read()
        assert (
            "postgres:15" in content
        ), "PostgreSQL service not found in docker-compose.yml"

    pyproject_path = "test-drf-postgresql/pyproject.toml"
    if os.path.exists(pyproject_path):
        with open(pyproject_path, "r") as f:
            content = f.read()
            assert (
                "psycopg2-binary" in content
            ), "psycopg2-binary not found in pyproject.toml"


def test_docker_build():
    """Test Docker build configuration."""
    if os.path.exists("test-docker-build"):
        shutil.rmtree("test-docker-build")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "fastapi"

    cmd = """cookiecutter . --no-input \
        project_name="Docker Build" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="Docker build test" \
        db_type="sqlite" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"Failed to generate project: {stderr}"
    assert os.path.exists("docker-build"), "Docker build project directory not created"

    dockerfile_path = "docker-build/Dockerfile"
    assert os.path.exists(dockerfile_path), "Dockerfile not found"

    with open(dockerfile_path, "r") as f:
        content = f.read()
        assert "FROM python:3.12-slim" in content, "Dockerfile doesn't use Python 3.12"
        assert "uv" in content, "Dockerfile doesn't use uv"
        assert "uv sync" in content, "Dockerfile doesn't use uv sync"


def test_drf_functionality():
    """Test DRF functionality and Django check."""
    if os.path.exists("test-drf-func"):
        shutil.rmtree("test-drf-func")

    os.environ["COOKIECUTTER_FRAMEWORK"] = "drf"

    cmd = """cookiecutter . --no-input \
        project_name="DRFFunc" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="DRF func test" \
        db_type="sqlite" """

    returncode, stdout, stderr = run_command(cmd)
    assert returncode == 0, f"DRF generation failed: {stderr}"
    assert os.path.exists("drffunc"), "DRF func project directory not created"

    returncode, stdout, stderr = run_command("uv sync", cwd="drffunc")
    assert returncode == 0, f"DRF uv sync failed: {stderr}"

    returncode, stdout, stderr = run_command(
        "uv run python src/drffunc/manage.py check --settings=drffunc.config.settings",
        cwd="drffunc",
    )
    assert returncode == 0, f"DRF check failed: {stderr}"
