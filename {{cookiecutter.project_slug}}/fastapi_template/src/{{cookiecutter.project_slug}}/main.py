"""
FastAPI application entry point for {{cookiecutter.project_name}}.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from {{cookiecutter.project_slug}}.adapters.driving.api.routes import api_router  # type: ignore # noqa: E501
from {{cookiecutter.project_slug}}.config.settings import settings  # type: ignore # noqa: E501
from {{cookiecutter.project_slug}}.dependencies.container import Container  # type: ignore # noqa: E501

# Create FastAPI app
app = FastAPI(
    title="{{cookiecutter.project_name}}",
    description="{{cookiecutter.description}}",
    version="1.0.0",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize dependency injection container
container = Container()

# Include API routes
app.include_router(api_router)

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "{{cookiecutter.project_name}} is running"}

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.{{cookiecutter.project_slug}}.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
