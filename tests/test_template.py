#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys


def run_command(cmd, cwd=None):
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd, capture_output=True, text=True, check=True
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout, e.stderr


def test_fastapi_sqlite():
    print("Testing FastAPI with SQLite...")
    if os.path.exists("test-fastapi-sqlite"):
        shutil.rmtree("test-fastapi-sqlite")
    cmd = """cookiecutter . --no-input \
        project_name="Test FastAPI SQLite" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test FastAPI project with SQLite" \
        db_type="sqlite" """
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"Failed to generate FastAPI SQLite project: {stderr}")
        return False
    if not os.path.exists("test-fastapi-sqlite"):
        print("FastAPI SQLite project directory not created")
        return False
    expected_files = [
        "test-fastapi-sqlite/pyproject.toml",
        "test-fastapi-sqlite/src/test-fastapi-sqlite/main.py",
        "test-fastapi-sqlite/src/test-fastapi-sqlite/domain/entities/user.py",
        "test-fastapi-sqlite/src/test-fastapi-sqlite/domain/services/user_service.py",
        "test-fastapi-sqlite/Dockerfile",
    ]
    for file_path in expected_files:
        if not os.path.exists(file_path):
            print(f"Missing file: {file_path}")
            return False
    docker_compose_path = "test-fastapi-sqlite/docker-compose.yml"
    if os.path.exists(docker_compose_path):
        with open(docker_compose_path, "r") as f:
            content = f.read().strip()
            if content:
                print(
                    f"docker-compose.yml should be empty for SQLite, but contains: {content}"
                )
                return False
    print("Testing uv sync...")
    returncode, stdout, stderr = run_command("uv sync", cwd="test-fastapi-sqlite")
    if returncode != 0:
        print(f"uv sync failed: {stderr}")
        return False
    print("FastAPI SQLite test passed!")
    return True


def test_fastapi_postgresql():
    print("Testing FastAPI with PostgreSQL...")
    if os.path.exists("test-fastapi-postgresql"):
        shutil.rmtree("test-fastapi-postgresql")
    cmd = """cookiecutter . --no-input \
        project_name="Test FastAPI PostgreSQL" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test FastAPI project with PostgreSQL" \
        db_type="postgresql" """
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"Failed to generate FastAPI PostgreSQL project: {stderr}")
        return False
    if not os.path.exists("test-fastapi-postgresql"):
        print("FastAPI PostgreSQL project directory not created")
        return False
    docker_compose_path = "test-fastapi-postgresql/docker-compose.yml"
    if not os.path.exists(docker_compose_path):
        print("docker-compose.yml not created for PostgreSQL")
        return False
    with open(docker_compose_path, "r") as f:
        content = f.read()
        if "postgres:15" not in content:
            print("PostgreSQL service not found in docker-compose.yml")
            return False
    pyproject_path = "test-fastapi-postgresql/pyproject.toml"
    if os.path.exists(pyproject_path):
        with open(pyproject_path, "r") as f:
            content = f.read()
            if "psycopg2-binary" not in content:
                print("psycopg2-binary not found in pyproject.toml")
                return False
    print("FastAPI PostgreSQL test passed!")
    return True


def test_drf_sqlite():
    print("Testing DRF with SQLite...")
    if os.path.exists("test-drf-sqlite"):
        shutil.rmtree("test-drf-sqlite")
    cmd = """cookiecutter . --no-input \
        project_name="Test DRF SQLite" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test DRF project with SQLite" \
        db_type="sqlite" """
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"Failed to generate DRF SQLite project: {stderr}")
        return False
    if not os.path.exists("test-drf-sqlite"):
        print("DRF SQLite project directory not created")
        return False
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
        if not os.path.exists(file_path):
            print(f"Missing file: {file_path}")
            return False
    docker_compose_path = "test-drf-sqlite/docker-compose.yml"
    if os.path.exists(docker_compose_path):
        with open(docker_compose_path, "r") as f:
            content = f.read().strip()
            if content:
                print(
                    f"docker-compose.yml should be empty for SQLite, but contains: {content}"
                )
                return False
    print("Testing uv sync...")
    returncode, stdout, stderr = run_command("uv sync", cwd="test-drf-sqlite")
    if returncode != 0:
        print(f"uv sync failed: {stderr}")
        return False
    print("DRF SQLite test passed!")
    return True


def test_drf_postgresql():
    print("Testing DRF with PostgreSQL...")
    if os.path.exists("test-drf-postgresql"):
        shutil.rmtree("test-drf-postgresql")
    cmd = """cookiecutter . --no-input \
        project_name="Test DRF PostgreSQL" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="A test DRF project with PostgreSQL" \
        db_type="postgresql" """
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"Failed to generate DRF PostgreSQL project: {stderr}")
        return False
    if not os.path.exists("test-drf-postgresql"):
        print("DRF PostgreSQL project directory not created")
        return False
    docker_compose_path = "test-drf-postgresql/docker-compose.yml"
    if not os.path.exists(docker_compose_path):
        print("docker-compose.yml not created for PostgreSQL")
        return False
    with open(docker_compose_path, "r") as f:
        content = f.read()
        if "postgres:15" not in content:
            print("PostgreSQL service not found in docker-compose.yml")
            return False
    pyproject_path = "test-drf-postgresql/pyproject.toml"
    if os.path.exists(pyproject_path):
        with open(pyproject_path, "r") as f:
            content = f.read()
            if "psycopg2-binary" not in content:
                print("psycopg2-binary not found in pyproject.toml")
                return False
    print("DRF PostgreSQL test passed!")
    return True


def test_docker_build():
    print("Testing Docker build...")
    if os.path.exists("test-docker-build"):
        shutil.rmtree("test-docker-build")
    cmd = """cookiecutter . --no-input \
        project_name="Docker Build" \
        framework="fastapi" \
        author_name="Test User" \
        email="test@example.com" \
        description="Docker build test" \
        db_type="sqlite" """
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"Failed to generate project: {stderr}")
        return False
    if not os.path.exists("docker-build"):
        print("Docker build project directory not created")
        return False
    dockerfile_path = "docker-build/Dockerfile"
    if not os.path.exists(dockerfile_path):
        print("Dockerfile not found")
        return False
    with open(dockerfile_path, "r") as f:
        content = f.read()
        if "FROM python:3.12-slim" not in content:
            print("Dockerfile doesn't use Python 3.12")
            return False
        if "uv" not in content:
            print("Dockerfile doesn't use uv")
            return False
        if "uv sync" not in content:
            print("Dockerfile doesn't use uv sync")
            return False
    print("Docker build test passed!")
    return True


def test_drf_functionality():
    print("Testing DRF functionality...")
    if os.path.exists("test-drf-func"):
        shutil.rmtree("test-drf-func")
    cmd = """cookiecutter . --no-input \
        project_name="DRF Func" \
        framework="drf" \
        author_name="Test User" \
        email="test@example.com" \
        description="DRF func test" \
        db_type="sqlite" """
    returncode, stdout, stderr = run_command(cmd)
    if returncode != 0:
        print(f"DRF generation failed: {stderr}")
        return False
    if not os.path.exists("drf-func"):
        print("DRF func project directory not created")
        return False
    returncode, stdout, stderr = run_command("uv sync", cwd="drf-func")
    if returncode != 0:
        print(f"DRF uv sync failed: {stderr}")
        return False
    returncode, stdout, stderr = run_command(
        "uv run python src/drf-func/manage.py check --settings=drf-func.config.settings",
        cwd="drf-func",
    )
    if returncode != 0:
        print(f"DRF check failed: {stderr}")
        return False
    print("DRF functionality test passed!")
    return True


def cleanup():
    print("Cleaning up test projects...")
    test_projects = [
        "test-fastapi-sqlite",
        "test-fastapi-postgresql",
        "test-drf-sqlite",
        "test-drf-postgresql",
        "docker-build",
        "drf-func",
        "debug-drf",
        "debug-test",
    ]
    for project in test_projects:
        if os.path.exists(project):
            shutil.rmtree(project)
            print(f"  Removed {project}")


def main():
    print("Starting cookiecutter template tests...")
    print("=" * 50)
    tests = [
        test_fastapi_sqlite,
        test_fastapi_postgresql,
        test_drf_sqlite,
        test_drf_postgresql,
        test_docker_build,
        test_drf_functionality,
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
            print(f"Test {test.__name__} failed with exception: {e}")
            failed += 1
        print()
    print("=" * 50)
    print(f"Test Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed!")
        return 1


if __name__ == "__main__":
    try:
        exit_code = main()
    finally:
        cleanup()
    sys.exit(exit_code)
