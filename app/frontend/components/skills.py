"""
Skills section component
"""
from nicegui import ui
from app.core.config import config

def create_skills_section():
    """Create the skills section of the portfolio."""
    
    # Skills section container
    with ui.column().classes('w-full py-20 bg-gray-50').id('skills'):
        with ui.column().classes('container mx-auto max-w-4xl px-4'):
            # Section title
            ui.label('My Skills').classes('section-title')
            
            # Skills introduction
            ui.label('Specialized in MERN Stack Development with expertise in:').classes('text-center mb-12 text-lg')
            
            # Skills categories
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'):
                # Generate skill cards for each category
                for skill_category in config.skills:
                    with ui.card().classes('p-6 h-full'):
                        ui.label(skill_category['category']).classes('text-xl font-bold mb-4 text-primary')
                        
                        # Skills list
                        with ui.column().classes('gap-2'):
                            for skill in skill_category['items']:
                                with ui.row().classes('items-center gap-2'):
                                    ui.icon('check_circle').classes('text-success-color')
                                    ui.label(skill)
            
            # MERN stack highlight
            with ui.card().classes('mt-12 p-6 bg-gradient-to-r from-blue-500 to-indigo-600 text-white'):
                ui.label('MERN Stack Expertise').classes('text-xl font-bold mb-4')
                
                with ui.row().classes('grid grid-cols-1 md:grid-cols-4 gap-6 mt-4'):
                    with ui.column().classes('items-center'):
                        ui.label('M').classes('text-4xl font-bold')
                        ui.label('MongoDB').classes('text-lg')
                        ui.label('NoSQL Database').classes('text-sm opacity-80')
                    
                    with ui.column().classes('items-center'):
                        ui.label('E').classes('text-4xl font-bold')
                        ui.label('Express.js').classes('text-lg')
                        ui.label('Backend Framework').classes('text-sm opacity-80')
                    
                    with ui.column().classes('items-center'):
                        ui.label('R').classes('text-4xl font-bold')
                        ui.label('React.js').classes('text-lg')
                        ui.label('Frontend Library').classes('text-sm opacity-80')
                    
                    with ui.column().classes('items-center'):
                        ui.label('N').classes('text-4xl font-bold')
                        ui.label('Node.js').classes('text-lg')
                        ui.label('JavaScript Runtime').classes('text-sm opacity-80')