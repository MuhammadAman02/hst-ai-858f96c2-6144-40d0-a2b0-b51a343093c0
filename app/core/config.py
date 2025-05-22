"""
Configuration settings for the portfolio application
"""
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List, Dict, Any, Optional
import os

class AppConfig(BaseSettings):
    """Application configuration with validation."""
    
    # Developer Information
    developer_name: str = Field(default="John Doe", description="Developer's full name")
    developer_title: str = Field(default="MERN Stack Developer", description="Developer's professional title")
    developer_email: str = Field(default="john.doe@example.com", description="Contact email")
    developer_location: str = Field(default="New York, NY", description="Developer's location")
    developer_github: str = Field(default="https://github.com/johndoe", description="GitHub profile URL")
    developer_linkedin: str = Field(default="https://linkedin.com/in/johndoe", description="LinkedIn profile URL")
    
    # Application Settings
    debug: bool = Field(default=False, description="Debug mode")
    log_level: str = Field(default="INFO", description="Logging level")
    
    # Portfolio Content
    about_me: str = Field(
        default="I am a passionate MERN Stack Developer with expertise in building modern web applications using MongoDB, Express.js, React.js, and Node.js. I focus on creating responsive, user-friendly applications with clean, maintainable code.",
        description="About me text"
    )
    
    skills: List[Dict[str, Any]] = Field(
        default=[
            {"category": "Frontend", "items": ["React.js", "Redux", "JavaScript (ES6+)", "TypeScript", "HTML5", "CSS3", "Sass", "Bootstrap", "Material UI", "Responsive Design"]},
            {"category": "Backend", "items": ["Node.js", "Express.js", "RESTful APIs", "GraphQL", "JWT Authentication"]},
            {"category": "Database", "items": ["MongoDB", "Mongoose ODM", "SQL", "Firebase"]},
            {"category": "DevOps & Tools", "items": ["Git", "GitHub", "Docker", "AWS", "Heroku", "Netlify", "Vercel", "Webpack", "npm/yarn"]},
            {"category": "Testing", "items": ["Jest", "React Testing Library", "Mocha", "Chai"]},
            {"category": "Methodologies", "items": ["Agile/Scrum", "CI/CD", "TDD", "Responsive Design", "RESTful Architecture"]}
        ],
        description="Developer skills by category"
    )
    
    projects: List[Dict[str, Any]] = Field(
        default=[
            {
                "title": "E-Commerce Platform",
                "description": "A full-featured e-commerce platform with product catalog, shopping cart, user authentication, and payment processing.",
                "technologies": ["React", "Node.js", "Express", "MongoDB", "Redux", "Stripe API"],
                "image": "ecommerce.jpg",
                "github_url": "https://github.com/johndoe/ecommerce-mern",
                "live_url": "https://ecommerce-mern-demo.herokuapp.com"
            },
            {
                "title": "Social Media Dashboard",
                "description": "A social media management dashboard allowing users to schedule and analyze posts across multiple platforms.",
                "technologies": ["React", "Node.js", "Express", "MongoDB", "Chart.js", "Social Media APIs"],
                "image": "social-dashboard.jpg",
                "github_url": "https://github.com/johndoe/social-dashboard",
                "live_url": "https://social-dashboard-demo.netlify.app"
            },
            {
                "title": "Task Management System",
                "description": "A collaborative task management system with real-time updates, task assignment, and progress tracking.",
                "technologies": ["React", "Node.js", "Express", "MongoDB", "Socket.io", "JWT"],
                "image": "task-manager.jpg",
                "github_url": "https://github.com/johndoe/task-manager-mern",
                "live_url": "https://task-manager-mern-demo.vercel.app"
            }
        ],
        description="Portfolio projects"
    )
    
    experience: List[Dict[str, Any]] = Field(
        default=[
            {
                "position": "Senior MERN Stack Developer",
                "company": "Tech Innovations Inc.",
                "location": "New York, NY",
                "period": "2021 - Present",
                "description": "Lead developer for multiple client projects using the MERN stack. Implemented CI/CD pipelines and mentored junior developers.",
                "achievements": [
                    "Reduced application load time by 40% through code optimization and lazy loading",
                    "Implemented microservices architecture that improved scalability",
                    "Led team of 5 developers to deliver projects consistently ahead of schedule"
                ]
            },
            {
                "position": "Full Stack Developer",
                "company": "Digital Solutions LLC",
                "location": "Boston, MA",
                "period": "2018 - 2021",
                "description": "Developed and maintained web applications for clients in finance and healthcare sectors using MERN stack.",
                "achievements": [
                    "Created a secure patient portal that complied with HIPAA regulations",
                    "Integrated payment processing systems for multiple e-commerce platforms",
                    "Implemented responsive designs that increased mobile user engagement by 35%"
                ]
            },
            {
                "position": "Frontend Developer",
                "company": "WebCraft Studios",
                "location": "Remote",
                "period": "2016 - 2018",
                "description": "Focused on creating responsive and interactive user interfaces using React.js and modern JavaScript.",
                "achievements": [
                    "Converted legacy jQuery applications to modern React architecture",
                    "Developed reusable component library that accelerated development time",
                    "Implemented state management solutions using Redux and Context API"
                ]
            }
        ],
        description="Work experience"
    )
    
    education: List[Dict[str, Any]] = Field(
        default=[
            {
                "degree": "Master of Science in Computer Science",
                "institution": "New York University",
                "location": "New York, NY",
                "period": "2014 - 2016",
                "description": "Specialized in Web Technologies and Distributed Systems"
            },
            {
                "degree": "Bachelor of Science in Software Engineering",
                "institution": "Boston University",
                "location": "Boston, MA",
                "period": "2010 - 2014",
                "description": "Graduated with honors. Relevant coursework included Database Systems, Algorithms, and Web Development."
            }
        ],
        description="Educational background"
    )
    
    testimonials: List[Dict[str, Any]] = Field(
        default=[
            {
                "name": "Sarah Johnson",
                "position": "CTO, Tech Innovations",
                "company": "Tech Innovations Inc.",
                "text": "John is an exceptional developer who consistently delivers high-quality code. His expertise in the MERN stack has been invaluable to our team.",
                "image": "testimonial1.jpg"
            },
            {
                "name": "Michael Chen",
                "position": "Product Manager",
                "company": "Digital Solutions LLC",
                "text": "Working with John was a pleasure. He not only understood our technical requirements but also provided valuable insights to improve our product.",
                "image": "testimonial2.jpg"
            },
            {
                "name": "Emily Rodriguez",
                "position": "Founder",
                "company": "StartUp Ventures",
                "text": "John transformed our concept into a fully functional application in record time. His knowledge of the MERN stack and attention to detail are impressive.",
                "image": "testimonial3.jpg"
            }
        ],
        description="Client and colleague testimonials"
    )
    
    # Server Settings
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Global configuration instance
config = AppConfig()