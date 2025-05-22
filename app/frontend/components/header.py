"""
Header component with navigation
"""
from nicegui import ui
from app.core.config import config

def create_header():
    """Create the header with navigation menu."""
    
    # Header container
    with ui.header().classes('w-full flex justify-between items-center px-4 py-3 bg-white shadow-md'):
        # Logo/Name
        with ui.link(target='/').classes('no-underline'):
            ui.label(config.developer_name).classes('text-xl font-bold text-primary')
        
        # Navigation - Desktop
        with ui.row().classes('gap-6 hidden md:flex'):
            ui.link('Home', target='#hero').classes('no-underline text-dark hover:text-primary transition-colors')
            ui.link('About', target='#about').classes('no-underline text-dark hover:text-primary transition-colors')
            ui.link('Skills', target='#skills').classes('no-underline text-dark hover:text-primary transition-colors')
            ui.link('Projects', target='#projects').classes('no-underline text-dark hover:text-primary transition-colors')
            ui.link('Experience', target='#experience').classes('no-underline text-dark hover:text-primary transition-colors')
            ui.link('Contact', target='#contact').classes('no-underline text-dark hover:text-primary transition-colors')
        
        # Mobile menu button
        menu_button = ui.button(icon='menu').props('flat').classes('md:hidden')
        
        # Mobile navigation drawer
        with ui.drawer(value=False).classes('bg-white') as drawer:
            with ui.column().classes('p-4 gap-4'):
                ui.label(config.developer_name).classes('text-xl font-bold text-primary mb-6')
                
                # Mobile navigation links
                ui.link('Home', target='#hero').classes('no-underline text-dark hover:text-primary transition-colors w-full')
                ui.link('About', target='#about').classes('no-underline text-dark hover:text-primary transition-colors w-full')
                ui.link('Skills', target='#skills').classes('no-underline text-dark hover:text-primary transition-colors w-full')
                ui.link('Projects', target='#projects').classes('no-underline text-dark hover:text-primary transition-colors w-full')
                ui.link('Experience', target='#experience').classes('no-underline text-dark hover:text-primary transition-colors w-full')
                ui.link('Contact', target='#contact').classes('no-underline text-dark hover:text-primary transition-colors w-full')
        
        # Connect menu button to drawer
        menu_button.on('click', drawer.toggle)