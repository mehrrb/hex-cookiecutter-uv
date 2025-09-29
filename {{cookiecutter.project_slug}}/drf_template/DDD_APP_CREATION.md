# DDD App Creation Guide

This project includes a custom Django management command to create apps with Domain-Driven Design (DDD) structure.

## Prerequisites

This project uses `uv` for dependency management. Make sure you have `uv` installed:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Run migrations**:
   ```bash
   uv run python manage.py migrate
   ```

## Usage

### Basic Usage
```bash
uv run python manage.py create_ddd_app <app_name>
```

### With Custom Service Name
```bash
uv run python manage.py create_ddd_app <app_name> --service-name <service_name>
```

## Examples

### Create a User Management Service
```bash
uv run python manage.py create_ddd_app user --service-name user_management
```

This creates:
```
src/user_management_service/
├── domain/
│   ├── entities/
│   │   └── user.py
│   ├── services/
│   │   └── user_service.py
│   └── repositories/
│       └── user_repository.py
├── application/
│   ├── services/
│   │   └── user_application_service.py
│   └── dto/
│       └── user_dto.py
├── infrastructure/
│   ├── user/              # Django app
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   └── ...
│   ├── repositories/
│   ├── external_services/
│   └── persistence/
└── presentation/
    ├── api/
    │   ├── user_views.py
    │   └── user_urls.py
    └── serializers/
        └── user_serializer.py
```

## What the Command Does

1. **Creates DDD Structure**: Sets up domain, application, infrastructure, and presentation layers
2. **Creates Django App**: Uses `startapp` to create the Django app in the infrastructure layer
3. **Generates Domain Files**: Creates entities, repositories, and domain services
4. **Generates Application Files**: Creates DTOs and application services
5. **Generates Presentation Files**: Creates serializers, views, and URL patterns
6. **Updates Settings**: Reminds you to add the app to `INSTALLED_APPS`

## Next Steps After Creation

1. **Add to Settings**:
   ```python
   # In settings.py
   INSTALLED_APPS = [
       # ... other apps
       'your_service.infrastructure.your_app',
   ]
   ```

2. **Run Migrations**:
   ```bash
   uv run python manage.py makemigrations your_app
   uv run python manage.py migrate
   ```

3. **Implement Business Logic**:
   - Update domain entities with your fields
   - Implement repository interfaces in infrastructure
   - Add business rules in domain services
   - Create application services for use cases

4. **Wire Up Dependencies**:
   - Configure dependency injection
   - Connect application services to domain services
   - Connect infrastructure repositories to domain interfaces

## Architecture Benefits

- **Separation of Concerns**: Each layer has a specific responsibility
- **Testability**: Easy to unit test each layer independently
- **Maintainability**: Clear boundaries between business logic and infrastructure
- **Scalability**: Easy to add new features without affecting existing code
- **Django Integration**: Leverages Django's ORM and admin while maintaining clean architecture

## File Structure Explanation

### Domain Layer
- **Entities**: Core business objects
- **Services**: Business logic and rules
- **Repositories**: Interfaces for data access

### Application Layer
- **Services**: Use cases and application logic
- **DTOs**: Data transfer objects for API communication

### Infrastructure Layer
- **Django App**: Models, migrations, admin
- **Repositories**: Concrete implementations of domain repositories
- **External Services**: Third-party integrations

### Presentation Layer
- **API Views**: REST endpoints
- **Serializers**: Data validation and transformation
- **URLs**: URL routing

This structure ensures that your Django project maintains clean architecture principles while leveraging Django's powerful features.
