"""
MERN Stack Developer Portfolio - Main Entry Point
"""
import os
from nicegui import ui, app
from app.frontend.portfolio_app import create_portfolio_app
from app.core.config import config

# Initialize the portfolio application
portfolio_app = create_portfolio_app()

# Configure app settings
app.title = f"{config.developer_name} - MERN Stack Developer"
app.favicon = "💻"

if __name__ == "__main__":
    # Get port from environment or use default
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    # Run the application
    ui.run(host=host, port=port, title=f"{config.developer_name} - MERN Stack Developer")