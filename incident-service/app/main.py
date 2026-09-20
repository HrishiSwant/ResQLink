from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from .database import client
from .rate_limit import limiter
from .routers.auth import router as auth_router
from .routers.incidents import router as incident_router


app = FastAPI(
    title="ResQLink - Incident Service",
    description="Incident management microservice",
    version="1.0.0"
)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.include_router(auth_router)
app.include_router(incident_router)


@app.get("/", tags=["Health"])
def root():
    return {
        "service": "Incident Service",
        "status": "running"
    }


@app.get("/health", tags=["Health"])
def health():
    try:
        client.admin.command("ping")

        return {
            "service": "Incident Service",
            "status": "healthy",
            "database": "connected"
        }

    except Exception:
        return {
            "service": "Incident Service",
            "status": "unhealthy",
            "database": "disconnected"
        }