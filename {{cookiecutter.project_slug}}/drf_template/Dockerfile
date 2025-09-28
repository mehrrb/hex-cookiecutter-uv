FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

        # Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
            gcc \
            libpq-dev \
            && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml ./

# Install dependencies with uv
RUN uv sync --frozen

# Copy application code
COPY . .

# Collect static files
RUN uv run python src/{{cookiecutter.project_slug}}/manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "python", "src/{{cookiecutter.project_slug}}/manage.py", "runserver", "0.0.0.0:8000"]
