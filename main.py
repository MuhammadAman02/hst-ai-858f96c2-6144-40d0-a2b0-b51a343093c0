"""
ML Engineer Portfolio - Main Entry Point
"""
import os
from nicegui import ui, app
from app.frontend.portfolio_app import create_portfolio_app
from app.core.config import config

# Initialize the portfolio application
portfolio_app = create_portfolio_app()

# Configure app settings
app.title = f"{config.developer_name} - Machine Learning Engineer"
app.favicon = "🧠"

if __name__ == "__main__":
    # Get port from environment or use default
    port = int(os.getenv("PORT", config.port))
    host = os.getenv("HOST", config.host)
    
    # Run the application
    ui.run(
        host=host, 
        port=port, 
        title=f"{config.developer_name} - Machine Learning Engineer",
        dark=config.dark_mode
    )