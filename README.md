# Hexagonal Architecture Cookiecutter Template

A modern Python project template using Hexagonal Architecture (Ports & Adapters) with support for FastAPI and Django REST Framework.

## Features

- 🏗️ **Hexagonal Architecture** - Clean separation of concerns
- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🎯 **Django REST Framework** - Powerful toolkit for building Web APIs
- 🏛️ **DDD Support** - Custom management command for Domain-Driven Design apps
- 🐍 **Python 3.12+** - Latest Python features
- 📦 **uv** - Fast Python package manager
- 🐳 **Docker** - Containerization support
- 🗄️ **Database Support** - SQLite and PostgreSQL
- 🧪 **Testing** - pytest with comprehensive test coverage
- 🔧 **Code Quality** - Black, Ruff, MyPy, Pre-commit

## Quick Start

```bash
# Install cookiecutter
pip install cookiecutter

# Generate a new project
cookiecutter https://github.com/your-username/hex-cookiecutter-uv.git
```

## Project Structure

```
your-project/
├── src/
│   └── your-project/
│       ├── domain/           # Business logic
│       │   ├── entities/     # Domain entities
│       │   └── services/     # Domain services
│       ├── adapters/         # External interfaces
│       │   ├── driving/      # Inbound adapters (API, CLI)
│       │   └── driven/       # Outbound adapters (DB, External APIs)
│       └── config/           # Configuration
├── pyproject.toml           # Project dependencies
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Multi-container setup
└── .env                    # Environment variables
```

## DDD App Creation (Django REST Framework)

For Django REST Framework projects, you can create new apps with Domain-Driven Design structure:

```bash
# Create a new DDD app
python manage.py create_ddd_app <app_name>

# Create with custom service name
python manage.py create_ddd_app <app_name> --service-name <service_name>
```

### Example

```bash
# Create a product management service
python manage.py create_ddd_app product --service-name product_management
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

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Format code
uv run black .

# Lint code
uv run ruff check .

# Type check
uv run mypy .
```

## License

MIT License - see LICENSE file for details.
