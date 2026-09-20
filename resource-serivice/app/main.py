from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from .database import client
from .rate_limit import limiter
from .routers.resources import router as resource_router


app = FastAPI(
    title="ResQLink - Resource Service",
    description="Emergency resource management microservice",
    version="1.0.0"
)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.include_router(resource_router)


@app.get("/", tags=["Health"])
def root():
    return {
        "service": "Resource Service",
        "status": "running"
    }


@app.get("/health", tags=["Health"])
def health():
    try:
        client.admin.command("ping")

        return {
            "service": "Resource Service",
            "status": "healthy",
            "database": "connected"
        }

    except Exception:
        return {
            "service": "Resource Service",
            "status": "unhealthy",
            "database": "disconnected"
        }