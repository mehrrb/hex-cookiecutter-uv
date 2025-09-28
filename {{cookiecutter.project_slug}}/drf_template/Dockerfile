FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Install system dependencies
{%- if cookiecutter.db_type == "postgresql" %}
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
{%- elif cookiecutter.db_type == "mysql" %}
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
{%- endif %}

# Copy project files
COPY pyproject.toml ./

# Install dependencies with uv
RUN uv sync --frozen

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "python", "src/{{cookiecutter.project_slug}}/manage.py", "runserver", "0.0.0.0:8000"]
