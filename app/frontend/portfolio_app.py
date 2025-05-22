"""
ML Engineer Portfolio - Frontend Application
"""
from nicegui import ui, app
from app.core.config import config
import datetime

class PortfolioApp:
    """ML Engineer Portfolio Application."""
    
    def __init__(self):
        """Initialize the portfolio application."""
        self.setup_routes()
        self.setup_theme()
    
    def setup_theme(self):
        """Configure application theme and styling."""
        # Set up dark/light mode
        app.add_static_files('/static', 'app/static')
        
        # Add custom CSS
        ui.add_head_html(f'''
        <style>
            :root {{
                --primary-color: {config.theme_color};
                --secondary-color: {config.secondary_color};
            }}
            
            .section-title {{
                font-size: 2rem;
                font-weight: 700;
                margin-bottom: 1.5rem;
                color: var(--primary-color);
            }}
            
            .card-hover:hover {{
                transform: translateY(-5px);
                transition: transform 0.3s ease;
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            }}
            
            .skill-tag {{
                background-color: var(--primary-color);
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.875rem;
                margin-right: 0.5rem;
                margin-bottom: 0.5rem;
                display: inline-block;
            }}
            
            .tech-tag {{
                background-color: var(--secondary-color);
                color: white;
                padding: 0.15rem 0.5rem;
                border-radius: 9999px;
                font-size: 0.75rem;
                margin-right: 0.25rem;
                margin-bottom: 0.25rem;
                display: inline-block;
            }}
            
            .timeline-item {{
                position: relative;
                padding-left: 2rem;
                padding-bottom: 2rem;
                border-left: 2px solid var(--primary-color);
            }}
            
            .timeline-item::before {{
                content: '';
                position: absolute;
                left: -0.5rem;
                top: 0;
                width: 1rem;
                height: 1rem;
                border-radius: 50%;
                background-color: var(--primary-color);
            }}
            
            .publication-card {{
                border-left: 4px solid var(--primary-color);
                padding-left: 1rem;
                margin-bottom: 1.5rem;
            }}
            
            @media (max-width: 768px) {{
                .responsive-col {{
                    flex-direction: column !important;
                }}
                
                .responsive-col > * {{
                    width: 100% !important;
                }}
            }}
        </style>
        ''')
    
    def setup_routes(self):
        """Set up application routes."""
        @ui.page('/')
        def home_page():
            """Render the home page."""
            self.create_home_layout()
        
        @ui.page('/projects')
        def projects_page():
            """Render the projects page."""
            self.create_projects_layout()
        
        @ui.page('/publications')
        def publications_page():
            """Render the publications page."""
            self.create_publications_layout()
        
        @ui.page('/experience')
        def experience_page():
            """Render the experience page."""
            self.create_experience_layout()
    
    def create_navigation(self):
        """Create the navigation menu."""
        with ui.header().classes('flex justify-between items-center p-4 bg-gray-800 text-white'):
            ui.label(config.developer_name).classes('text-xl font-bold')
            
            with ui.row().classes('gap-4'):
                ui.button('Home', on_click=lambda: ui.navigate.to('/')).props('flat color=white')
                ui.button('Projects', on_click=lambda: ui.navigate.to('/projects')).props('flat color=white')
                ui.button('Publications', on_click=lambda: ui.navigate.to('/publications')).props('flat color=white')
                ui.button('Experience', on_click=lambda: ui.navigate.to('/experience')).props('flat color=white')
                
                # Dark/Light mode toggle
                dark = ui.dark_mode()
                ui.button(on_click=lambda: dark.toggle(), icon='dark_mode').props('flat color=white')
    
    def create_footer(self):
        """Create the footer section."""
        current_year = datetime.datetime.now().year
        with ui.footer().classes('p-4 bg-gray-800 text-white text-center'):
            ui.label(f'© {current_year} {config.developer_name}. All rights reserved.').classes('text-sm')
            
            with ui.row().classes('justify-center gap-4 mt-2'):
                if config.github_url:
                    ui.link('GitHub', config.github_url).classes('text-white hover:text-blue-300')
                if config.linkedin_url:
                    ui.link('LinkedIn', config.linkedin_url).classes('text-white hover:text-blue-300')
                if config.twitter_url:
                    ui.link('Twitter', config.twitter_url).classes('text-white hover:text-blue-300')
                if config.kaggle_url:
                    ui.link('Kaggle', config.kaggle_url).classes('text-white hover:text-blue-300')
                if config.google_scholar_url:
                    ui.link('Google Scholar', config.google_scholar_url).classes('text-white hover:text-blue-300')
    
    def create_home_layout(self):
        """Create the home page layout."""
        self.create_navigation()
        
        # Hero Section
        with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
            with ui.row().classes('responsive-col items-center justify-between py-16 gap-8'):
                with ui.column().classes('w-1/2'):
                    ui.label(f"Hi, I'm {config.developer_name}").classes('text-4xl font-bold mb-2')
                    ui.label(config.developer_title).classes('text-2xl text-blue-600 mb-4')
                    ui.label(config.developer_bio).classes('text-lg mb-6')
                    
                    with ui.row().classes('gap-4'):
                        ui.button('View Projects', on_click=lambda: ui.navigate.to('/projects')).props('color=primary')
                        ui.button('Contact Me', on_click=lambda: ui.open(f'mailto:{config.developer_email}')).props('outline')
                
                with ui.column().classes('w-1/2 flex justify-center'):
                    # Placeholder for profile image - replace with actual image path
                    ui.image('https://via.placeholder.com/400x400').classes('rounded-full w-64 h-64 object-cover shadow-lg')
            
            # Skills Section
            ui.label('Skills & Expertise').classes('section-title mt-12')
            
            with ui.grid(columns=2).classes('gap-6'):
                for category, skills in config.skills.items():
                    with ui.card().classes('card-hover'):
                        ui.label(category).classes('text-xl font-bold mb-4')
                        with ui.element('div').classes('flex flex-wrap'):
                            for skill in skills:
                                ui.element('span').classes('skill-tag').text(skill)
            
            # Featured Projects Section
            ui.label('Featured Projects').classes('section-title mt-12')
            
            with ui.grid(columns=3).classes('gap-6'):
                # Display only the first 3 projects on the home page
                for project in config.projects[:3]:
                    with ui.card().classes('card-hover'):
                        # Project image
                        ui.image(f"https://via.placeholder.com/600x400?text={project['title']}").classes('w-full h-48 object-cover')
                        
                        with ui.card_section():
                            ui.label(project['title']).classes('text-xl font-bold mb-2')
                            ui.label(project['description']).classes('mb-4 text-sm')
                            
                            with ui.element('div').classes('flex flex-wrap mb-4'):
                                for tech in project['technologies'][:4]:  # Limit to 4 technologies
                                    ui.element('span').classes('tech-tag').text(tech)
                            
                            with ui.row().classes('justify-between'):
                                if project['github_url']:
                                    ui.link('GitHub', project['github_url']).classes('text-blue-600')
                                if project['demo_url']:
                                    ui.link('Demo', project['demo_url']).classes('text-blue-600')
            
            ui.button('View All Projects', on_click=lambda: ui.navigate.to('/projects')).classes('mt-6 mx-auto').props('outline')
            
            # Brief Experience Section
            ui.label('Experience').classes('section-title mt-12')
            
            with ui.column().classes('space-y-6'):
                # Show only the most recent experience
                for experience in config.experience[:2]:
                    with ui.card().classes('timeline-item'):
                        ui.label(experience['title']).classes('text-xl font-bold')
                        ui.label(f"{experience['company']} • {experience['location']}").classes('text-lg text-blue-600')
                        
                        end_date = experience['end_date'] if experience['end_date'] else 'Present'
                        ui.label(f"{experience['start_date']} - {end_date}").classes('text-sm text-gray-600 mb-2')
                        
                        ui.label(experience['description']).classes('text-sm')
            
            ui.button('View Full Experience', on_click=lambda: ui.navigate.to('/experience')).classes('mt-6 mx-auto').props('outline')
        
        self.create_footer()
    
    def create_projects_layout(self):
        """Create the projects page layout."""
        self.create_navigation()
        
        with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
            ui.label('ML Projects').classes('section-title mt-8')
            
            # Project filters
            with ui.row().classes('mb-6 gap-4'):
                ui.label('Filter by:').classes('self-center')
                ui.button('All', on_click=lambda: ui.notify('Filter: All')).props('outline')
                ui.button('Computer Vision', on_click=lambda: ui.notify('Filter: Computer Vision')).props('outline')
                ui.button('NLP', on_click=lambda: ui.notify('Filter: NLP')).props('outline')
                ui.button('Time Series', on_click=lambda: ui.notify('Filter: Time Series')).props('outline')
            
            # Projects grid
            with ui.grid(columns=2).classes('gap-8'):
                for project in config.projects:
                    with ui.card().classes('card-hover'):
                        # Project image
                        ui.image(f"https://via.placeholder.com/800x450?text={project['title']}").classes('w-full h-56 object-cover')
                        
                        with ui.card_section():
                            ui.label(project['title']).classes('text-2xl font-bold mb-2')
                            ui.label(project['description']).classes('mb-4')
                            
                            ui.label('Technologies:').classes('font-semibold mt-4 mb-2')
                            with ui.element('div').classes('flex flex-wrap mb-4'):
                                for tech in project['technologies']:
                                    ui.element('span').classes('tech-tag').text(tech)
                            
                            with ui.row().classes('justify-start gap-4 mt-4'):
                                if project['github_url']:
                                    ui.button('GitHub', on_click=lambda url=project['github_url']: ui.open(url)).props('outline')
                                if project['demo_url']:
                                    ui.button('Live Demo', on_click=lambda url=project['demo_url']: ui.open(url)).props('color=primary')
                                if project['paper_url']:
                                    ui.button('Research Paper', on_click=lambda url=project['paper_url']: ui.open(url)).props('outline color=secondary')
        
        self.create_footer()
    
    def create_publications_layout(self):
        """Create the publications page layout."""
        self.create_navigation()
        
        with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
            ui.label('Publications & Research').classes('section-title mt-8')
            
            with ui.column().classes('space-y-8'):
                for publication in config.publications:
                    with ui.card().classes('publication-card'):
                        ui.label(publication['title']).classes('text-xl font-bold mb-2')
                        ui.label(publication['authors']).classes('text-blue-600 mb-1')
                        ui.label(f"{publication['conference']} • {publication['year']}").classes('text-sm text-gray-600 mb-4')
                        
                        ui.button('Read Paper', on_click=lambda url=publication['url']: ui.open(url)).props('outline')
            
            # Research interests section
            ui.label('Research Interests').classes('section-title mt-12')
            
            with ui.grid(columns=3).classes('gap-6'):
                with ui.card().classes('card-hover'):
                    ui.label('Computer Vision').classes('text-xl font-bold mb-2')
                    ui.label('Medical imaging analysis, object detection, and image segmentation using deep learning approaches.').classes('text-sm')
                
                with ui.card().classes('card-hover'):
                    ui.label('Natural Language Processing').classes('text-xl font-bold mb-2')
                    ui.label('Transformer architectures, few-shot learning, and efficient fine-tuning methods for language models.').classes('text-sm')
                
                with ui.card().classes('card-hover'):
                    ui.label('ML Systems').classes('text-xl font-bold mb-2')
                    ui.label('Scalable machine learning systems, model optimization, and efficient deployment strategies.').classes('text-sm')
        
        self.create_footer()
    
    def create_experience_layout(self):
        """Create the experience page layout."""
        self.create_navigation()
        
        with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
            # Work Experience Section
            ui.label('Work Experience').classes('section-title mt-8')
            
            with ui.column().classes('space-y-8'):
                for experience in config.experience:
                    with ui.card().classes('timeline-item'):
                        ui.label(experience['title']).classes('text-xl font-bold')
                        ui.label(f"{experience['company']} • {experience['location']}").classes('text-lg text-blue-600')
                        
                        end_date = experience['end_date'] if experience['end_date'] else 'Present'
                        ui.label(f"{experience['start_date']} - {end_date}").classes('text-sm text-gray-600 mb-2')
                        
                        ui.label(experience['description']).classes('text-md')
            
            # Education Section
            ui.label('Education').classes('section-title mt-12')
            
            with ui.column().classes('space-y-8'):
                for education in config.education:
                    with ui.card().classes('timeline-item'):
                        ui.label(education['degree']).classes('text-xl font-bold')
                        ui.label(f"{education['institution']} • {education['location']}").classes('text-lg text-blue-600')
                        
                        ui.label(f"{education['start_year']} - {education['end_year']}").classes('text-sm text-gray-600 mb-2')
                        
                        ui.label(education['description']).classes('text-md')
            
            # Certifications Section
            ui.label('Certifications').classes('section-title mt-12')
            
            with ui.grid(columns=2).classes('gap-6'):
                with ui.card().classes('card-hover'):
                    ui.label('TensorFlow Developer Certificate').classes('text-xl font-bold mb-2')
                    ui.label('Google • 2022').classes('text-blue-600 mb-4')
                    ui.label('Demonstrated proficiency in building and training neural networks using TensorFlow.').classes('text-sm')
                
                with ui.card().classes('card-hover'):
                    ui.label('AWS Machine Learning Specialty').classes('text-xl font-bold mb-2')
                    ui.label('Amazon Web Services • 2021').classes('text-blue-600 mb-4')
                    ui.label('Expertise in designing, implementing, and deploying ML solutions on AWS.').classes('text-sm')
        
        self.create_footer()

def create_portfolio_app():
    """Create and return the portfolio application."""
    return PortfolioApp()