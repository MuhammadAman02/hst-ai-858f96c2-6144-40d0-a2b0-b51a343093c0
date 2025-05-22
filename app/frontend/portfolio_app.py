"""
MERN Stack Developer Portfolio - Main UI Application
"""
from nicegui import ui, app
from app.core.config import config
from app.frontend.components.header import create_header
from app.frontend.components.hero import create_hero_section
from app.frontend.components.about import create_about_section
from app.frontend.components.skills import create_skills_section
from app.frontend.components.projects import create_projects_section
from app.frontend.components.experience import create_experience_section
from app.frontend.components.education import create_education_section
from app.frontend.components.testimonials import create_testimonials_section
from app.frontend.components.contact import create_contact_section
from app.frontend.components.footer import create_footer

def create_portfolio_app():
    """Create and configure the portfolio application."""
    
    # Add custom CSS
    with ui.head():
        ui.add_css("""
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        :root {
            --primary-color: #3498db;
            --secondary-color: #2c3e50;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --text-color: #333;
            --text-light: #7f8c8d;
            --success-color: #2ecc71;
            --warning-color: #f39c12;
            --danger-color: #e74c3c;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            color: var(--text-color);
            line-height: 1.6;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        
        .section {
            padding: 80px 0;
        }
        
        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 50px;
            text-align: center;
            color: var(--dark-color);
            position: relative;
        }
        
        .section-title:after {
            content: '';
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background-color: var(--primary-color);
        }
        
        .card {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        }
        
        .btn-primary {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 5px;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .btn-primary:hover {
            background-color: #2980b9;
            transform: translateY(-2px);
        }
        
        .btn-outline {
            background-color: transparent;
            color: var(--primary-color);
            border: 2px solid var(--primary-color);
            padding: 10px 25px;
            border-radius: 5px;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .btn-outline:hover {
            background-color: var(--primary-color);
            color: white;
        }
        
        .text-primary {
            color: var(--primary-color);
        }
        
        .bg-primary {
            background-color: var(--primary-color);
        }
        
        .bg-light {
            background-color: var(--light-color);
        }
        
        .bg-dark {
            background-color: var(--dark-color);
            color: white;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .section {
                padding: 60px 0;
            }
            
            .section-title {
                font-size: 2rem;
            }
        }
        """)
    
    # Define pages
    @ui.page('/')
    def index():
        """Main portfolio page."""
        # Create header/navigation
        create_header()
        
        # Main content container
        with ui.column().classes('w-full'):
            # Hero section
            create_hero_section()
            
            # About section
            create_about_section()
            
            # Skills section
            create_skills_section()
            
            # Projects section
            create_projects_section()
            
            # Experience section
            create_experience_section()
            
            # Education section
            create_education_section()
            
            # Testimonials section
            create_testimonials_section()
            
            # Contact section
            create_contact_section()
            
            # Footer
            create_footer()
    
    # Return the configured app
    return app