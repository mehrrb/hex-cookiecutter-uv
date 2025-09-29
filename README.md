# Hexagonal Architecture Cookiecutter Template

A modern Python project template using Hexagonal Architecture (Ports & Adapters) with support for FastAPI and Django REST Framework. Built with `uv` for fast dependency management and development workflow.

## Features

- 🏗️ **Hexagonal Architecture** - Clean separation of concerns with ports & adapters
- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🎯 **Django REST Framework** - Powerful toolkit for building Web APIs
- 🏛️ **DDD Support** - Custom management command for Domain-Driven Design apps
- 🐍 **Python 3.12+** - Latest Python features and performance
- 📦 **uv** - Ultra-fast Python package manager and project manager
- 🐳 **Docker** - Complete containerization support with docker-compose
- 🗄️ **Database Support** - SQLite (development) and PostgreSQL (production)
- 🧪 **Testing** - pytest with comprehensive test coverage
- 🔧 **Code Quality** - Black, Ruff, MyPy, Pre-commit hooks
- 📚 **Documentation** - Comprehensive guides and examples

## Prerequisites

Before using this template, make sure you have:

- **Python 3.12+** installed
- **uv** package manager installed
- **cookiecutter** installed

### Install uv

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

### Install cookiecutter

```bash
pip install cookiecutter
```

## Quick Start

### 1. Create a New Project

```bash
# Clone and generate a new project
cookiecutter https://github.com/mehrrb/hex-cookiecutter-uv.git

# Or use the template directly
cookiecutter gh:mehrrb/hex-cookiecutter-uv
```

### 2. Choose Your Framework

The template will prompt you to select between:
- **FastAPI** - For modern, high-performance APIs
- **Django REST Framework** - For full-featured web applications

### 3. Set Up Your Project

```bash
# Navigate to your new project
cd your-project-name

# Install dependencies with uv
uv sync

# Run initial setup (Django projects)
uv run  manage.py migrate

# Start development server
uv run  manage.py runserver  # Django
# or
uv run  -m src.your_project.main  # FastAPI
```

## Architecture

This template implements **Hexagonal Architecture** (also known as Ports & Adapters), which provides:

- **Clean separation** between business logic and infrastructure
- **Testability** - Easy to unit test business logic in isolation
- **Flexibility** - Easy to swap out infrastructure components
- **Maintainability** - Clear boundaries and responsibilities

### Core Principles

1. **Domain Layer** - Contains pure business logic, no external dependencies
2. **Application Layer** - Orchestrates use cases and coordinates between domain and infrastructure
3. **Infrastructure Layer** - Handles external concerns (database, APIs, file system)
4. **Presentation Layer** - Handles user interface and API endpoints

## Project Structure

```
your-project/
├── src/
│   └── your-project/
│       ├── domain/           # Business logic (pure Python)
│       │   ├── entities/     # Domain entities
│       │   ├── services/     # Domain services
│       │   └── repositories/ # Repository interfaces
│       ├── adapters/         # External interfaces
│       │   ├── driving/      # Inbound adapters (API, CLI)
│       │   └── driven/       # Outbound adapters (DB, External APIs)
│       ├── config/           # Configuration
│       └── dependencies/     # Dependency injection
├── pyproject.toml           # Project dependencies and metadata
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Multi-container setup
├── scripts/                # Convenience scripts
└── .env                    # Environment variables
```

## DDD App Creation (Django REST Framework)

For Django REST Framework projects, you can create new apps with Domain-Driven Design structure using the built-in management command:

```bash
# Create a new DDD app
uv run  manage.py create_ddd_app <app_name>

# Create with custom service name
uv run  manage.py create_ddd_app <app_name> --service-name <service_name>

```

### Example

```bash
# Create a product management service
uv run  manage.py create_ddd_app product --service-name product_management

```

This creates a complete DDD structure:

```
src/product_management_service/
├── domain/
│   ├── entities/
│   │   └── product.py
│   ├── services/
│   │   └── product_service.py
│   └── repositories/
│       └── product_repository.py
├── application/
│   ├── services/
│   │   └── product_application_service.py
│   └── dto/
│       └── product_dto.py
├── infrastructure/
│   ├── product/              # Django app
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...
│   ├── repositories/
│   └── external_services/
└── presentation/
    ├── api/
    │   ├── product_views.py
    │   └── product_urls.py
    └── serializers/
        └── product_serializer.py
```

## Development

### Daily Development Commands

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Format code
uv run black .

# Lint code
uv run ruff check .

# Fix linting issues
uv run ruff check --fix .

# Type check
uv run mypy .

# Run all quality checks
uv run pre-commit run --all-files
```

### Database Management (Django)

```bash
# Create migrations
uv run  manage.py makemigrations

# Apply migrations
uv run  manage.py migrate

# Create superuser
uv run  manage.py createsuperuser

# Django shell
uv run  manage.py shell

# Django admin
uv run manage.py runserver
# Visit http://localhost:8000/admin
```

### Docker Development

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild containers
docker-compose up --build
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/your-username/hex-cookiecutter-uv.git
cd hex-cookiecutter-uv

# Install development dependencies
uv sync

# Run tests
uv run pytest

# Run pre-commit hooks
uv run pre-commit install
```
