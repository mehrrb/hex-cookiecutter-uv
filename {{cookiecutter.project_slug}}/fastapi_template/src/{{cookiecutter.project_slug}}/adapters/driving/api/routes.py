"""
FastAPI routes for {{cookiecutter.project_name}}.
"""

from fastapi import APIRouter

# Create API router
api_router = APIRouter(prefix="/api/v1")


@api_router.get("/")
async def api_root():
    """API root endpoint."""
    return {"message": "{{cookiecutter.project_name}} API", "version": "1.0.0"}


# Add your API routes here
# from .user_routes import router as user_router
# api_router.include_router(user_router, prefix="/users", tags=["users"])
