"""
About section component
"""
from nicegui import ui
from app.core.config import config

def create_about_section():
    """Create the about section of the portfolio."""
    
    # About section container
    with ui.column().classes('w-full py-20 bg-white').id('about'):
        with ui.column().classes('container mx-auto max-w-4xl px-4'):
            # Section title
            ui.label('About Me').classes('section-title')
            
            # About content
            with ui.row().classes('flex flex-col md:flex-row gap-8 items-center'):
                # Image column
                with ui.column().classes('md:w-1/3'):
                    ui.image('https://via.placeholder.com/400x500').classes('rounded-lg shadow-lg w-full')
                
                # Text column
                with ui.column().classes('md:w-2/3'):
                    ui.markdown(config.about_me).classes('text-lg mb-6')
                    
                    # Key facts/highlights
                    with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-4 mb-6'):
                        with ui.card().classes('p-4 bg-gray-50'):
                            ui.label('Location').classes('font-bold text-primary')
                            ui.label(config.developer_location)
                        
                        with ui.card().classes('p-4 bg-gray-50'):
                            ui.label('Experience').classes('font-bold text-primary')
                            ui.label('5+ Years')
                        
                        with ui.card().classes('p-4 bg-gray-50'):
                            ui.label('Availability').classes('font-bold text-primary')
                            ui.label('Full-time / Freelance')
                        
                        with ui.card().classes('p-4 bg-gray-50'):
                            ui.label('Remote Work').classes('font-bold text-primary')
                            ui.label('Available')
                    
                    # Download resume button
                    ui.button('Download Resume', icon='download').classes('btn-primary')