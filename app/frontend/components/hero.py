"""
Hero section component
"""
from nicegui import ui
from app.core.config import config

def create_hero_section():
    """Create the hero section of the portfolio."""
    
    # Hero section container
    with ui.column().classes('w-full min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-indigo-600 text-white p-4').id('hero'):
        with ui.column().classes('container mx-auto max-w-4xl text-center'):
            # Profile image (placeholder)
            ui.image('https://via.placeholder.com/150').classes('rounded-full w-32 h-32 mx-auto mb-6 border-4 border-white')
            
            # Name and title
            ui.label(config.developer_name).classes('text-4xl md:text-5xl font-bold mb-2')
            ui.label(config.developer_title).classes('text-xl md:text-2xl mb-6')
            
            # Brief intro
            ui.label("Building modern web applications with the MERN stack").classes('text-lg md:text-xl mb-8 max-w-2xl mx-auto')
            
            # CTA buttons
            with ui.row().classes('gap-4 justify-center flex-wrap'):
                ui.button('View Projects', on_click=lambda: ui.navigate.to('#projects')).classes('btn-primary text-lg')
                ui.button('Contact Me', on_click=lambda: ui.navigate.to('#contact')).classes('btn-outline text-lg')
            
            # Social links
            with ui.row().classes('gap-4 justify-center mt-8'):
                ui.link(target=config.developer_github, new_tab=True).classes('text-white hover:text-gray-200 transition-colors').style('font-size: 1.5rem;').on('click', lambda: None).tooltip('GitHub'):
                    ui.icon('fab fa-github')
                ui.link(target=config.developer_linkedin, new_tab=True).classes('text-white hover:text-gray-200 transition-colors').style('font-size: 1.5rem;').on('click', lambda: None).tooltip('LinkedIn'):
                    ui.icon('fab fa-linkedin')
                ui.link(f"mailto:{config.developer_email}", new_tab=True).classes('text-white hover:text-gray-200 transition-colors').style('font-size: 1.5rem;').on('click', lambda: None).tooltip('Email'):
                    ui.icon('fas fa-envelope')