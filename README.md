# Hexagonal Architecture Cookiecutter Template

A modern Python project template using Hexagonal Architecture (Ports & Adapters) with support for FastAPI and Django REST Framework.

## Features

- 🏗️ **Hexagonal Architecture** - Clean separation of concerns
- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🎯 **Django REST Framework** - Powerful toolkit for building Web APIs
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
