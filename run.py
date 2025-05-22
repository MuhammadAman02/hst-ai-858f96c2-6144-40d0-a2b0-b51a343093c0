"""
Alternative entry point for the ML Engineer Portfolio application.
This file provides more configuration options and can be used for production deployment.
"""
import os
import uvicorn
from app.core.config import config

def run_app():
    """Run the application using uvicorn directly."""
    # Get port from environment or use default
    port = int(os.getenv("PORT", config.port))
    host = os.getenv("HOST", config.host)
    
    # Run with uvicorn
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=config.debug,
        log_level="info" if not config.debug else "debug"
    )

if __name__ == "__main__":
    run_app()