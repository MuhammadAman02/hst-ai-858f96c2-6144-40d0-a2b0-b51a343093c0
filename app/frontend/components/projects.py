"""
Projects section component
"""
from nicegui import ui
from app.core.config import config

def create_projects_section():
    """Create the projects section of the portfolio."""
    
    # Projects section container
    with ui.column().classes('w-full py-20 bg-white').id('projects'):
        with ui.column().classes('container mx-auto max-w-4xl px-4'):
            # Section title
            ui.label('My Projects').classes('section-title')
            
            # Projects introduction
            ui.label('Showcasing my best work with the MERN stack').classes('text-center mb-12 text-lg')
            
            # Projects grid
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8'):
                # Generate project cards
                for project in config.projects:
                    with ui.card().classes('overflow-hidden h-full flex flex-col'):
                        # Project image
                        ui.image(f"https://via.placeholder.com/600x400?text={project['title']}").classes('w-full h-48 object-cover')
                        
                        # Project content
                        with ui.card_section().classes('p-4 flex-grow'):
                            ui.label(project['title']).classes('text-xl font-bold mb-2')
                            ui.label(project['description']).classes('mb-4 text-sm text-gray-600')
                            
                            # Technologies used
                            with ui.row().classes('flex flex-wrap gap-2 mb-4'):
                                for tech in project['technologies']:
                                    ui.label(tech).classes('px-2 py-1 bg-blue-100 text-blue-800 rounded-full text-xs')
                        
                        # Project links
                        with ui.card_section().classes('p-4 bg-gray-50 flex justify-between'):
                            ui.link('Live Demo', target=project['live_url'], new_tab=True).classes('btn-primary py-1 px-3 text-sm')
                            ui.link('GitHub', target=project['github_url'], new_tab=True).classes('btn-outline py-1 px-3 text-sm')
            
            # View more projects button
            with ui.row().classes('justify-center mt-12'):
                ui.link('View More on GitHub', target=config.developer_github, new_tab=True).classes('btn-primary')