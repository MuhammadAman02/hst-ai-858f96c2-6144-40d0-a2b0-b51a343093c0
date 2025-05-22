"""
Configuration settings for the ML Engineer Portfolio application.
"""
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List, Dict, Any, Optional
import os

class AppConfig(BaseSettings):
    """Application configuration with validation."""
    
    # Developer Information
    developer_name: str = Field(default="Jane Doe", description="ML Engineer name")
    developer_title: str = Field(default="Machine Learning Engineer", description="Professional title")
    developer_email: str = Field(default="jane.doe@example.com", description="Contact email")
    developer_location: str = Field(default="San Francisco, CA", description="Location")
    developer_bio: str = Field(
        default="Experienced Machine Learning Engineer specializing in computer vision and NLP with a track record of deploying models to production.",
        description="Short biography"
    )
    
    # Social Media Links
    github_url: str = Field(default="https://github.com/janedoe", description="GitHub profile URL")
    linkedin_url: str = Field(default="https://linkedin.com/in/janedoe", description="LinkedIn profile URL")
    twitter_url: Optional[str] = Field(default=None, description="Twitter profile URL")
    kaggle_url: Optional[str] = Field(default="https://kaggle.com/janedoe", description="Kaggle profile URL")
    google_scholar_url: Optional[str] = Field(default=None, description="Google Scholar profile URL")
    
    # Portfolio Settings
    theme_color: str = Field(default="#4F46E5", description="Primary theme color")
    secondary_color: str = Field(default="#818CF8", description="Secondary theme color")
    dark_mode: bool = Field(default=True, description="Enable dark mode by default")
    
    # ML Projects
    projects: List[Dict[str, Any]] = Field(
        default=[
            {
                "title": "Computer Vision for Medical Imaging",
                "description": "Developed a deep learning model to detect abnormalities in X-ray images with 94% accuracy.",
                "technologies": ["PyTorch", "TensorFlow", "OpenCV", "MONAI"],
                "image": "medical_imaging.jpg",
                "github_url": "https://github.com/janedoe/medical-imaging",
                "demo_url": None,
                "paper_url": "https://arxiv.org/abs/xxxx.xxxxx",
            },
            {
                "title": "NLP for Customer Support Automation",
                "description": "Built an intent classification system that reduced customer support response time by 45%.",
                "technologies": ["BERT", "Hugging Face", "spaCy", "FastAPI"],
                "image": "nlp_customer_support.jpg",
                "github_url": "https://github.com/janedoe/nlp-customer-support",
                "demo_url": "https://demo-nlp-support.example.com",
                "paper_url": None,
            },
            {
                "title": "Time Series Forecasting for Energy Consumption",
                "description": "Implemented a transformer-based model for predicting energy usage patterns with 30% lower error than traditional methods.",
                "technologies": ["PyTorch", "Prophet", "Pandas", "Darts"],
                "image": "time_series.jpg",
                "github_url": "https://github.com/janedoe/energy-forecasting",
                "demo_url": None,
                "paper_url": None,
            },
        ],
        description="List of ML projects"
    )
    
    # Skills
    skills: Dict[str, List[str]] = Field(
        default={
            "Machine Learning": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Deep Learning", "MLOps"],
            "Frameworks & Libraries": ["TensorFlow", "PyTorch", "scikit-learn", "Hugging Face", "OpenCV", "spaCy"],
            "Languages": ["Python", "SQL", "R", "C++"],
            "Tools & Platforms": ["Docker", "Kubernetes", "AWS", "GCP", "MLflow", "DVC", "Weights & Biases"],
            "Data Processing": ["Pandas", "NumPy", "PySpark", "Dask", "SQL"],
        },
        description="Skills categorized by domain"
    )
    
    # Publications
    publications: List[Dict[str, Any]] = Field(
        default=[
            {
                "title": "Advances in Medical Image Classification Using Attention Mechanisms",
                "authors": "Doe, J., Smith, A., Johnson, B.",
                "conference": "Conference on Computer Vision and Pattern Recognition (CVPR)",
                "year": 2022,
                "url": "https://example.com/paper1",
            },
            {
                "title": "Efficient Transformer Models for Resource-Constrained Environments",
                "authors": "Smith, A., Doe, J., Williams, C.",
                "conference": "Neural Information Processing Systems (NeurIPS)",
                "year": 2021,
                "url": "https://example.com/paper2",
            },
        ],
        description="Academic publications"
    )
    
    # Experience
    experience: List[Dict[str, Any]] = Field(
        default=[
            {
                "title": "Senior Machine Learning Engineer",
                "company": "AI Solutions Inc.",
                "location": "San Francisco, CA",
                "start_date": "2021-01",
                "end_date": None,  # None for current positions
                "description": "Leading a team of ML engineers to develop and deploy computer vision solutions for healthcare applications. Reduced model inference time by 40% and improved accuracy by 15%.",
            },
            {
                "title": "Machine Learning Engineer",
                "company": "Tech Innovations",
                "location": "Boston, MA",
                "start_date": "2018-06",
                "end_date": "2020-12",
                "description": "Developed NLP models for sentiment analysis and intent classification. Implemented MLOps practices that reduced deployment time from weeks to days.",
            },
            {
                "title": "Data Scientist",
                "company": "DataCorp",
                "location": "Seattle, WA",
                "start_date": "2016-08",
                "end_date": "2018-05",
                "description": "Built predictive models for customer churn and product recommendations. Created data pipelines that processed over 1TB of data daily.",
            },
        ],
        description="Work experience"
    )
    
    # Education
    education: List[Dict[str, Any]] = Field(
        default=[
            {
                "degree": "Ph.D. in Computer Science",
                "institution": "Stanford University",
                "location": "Stanford, CA",
                "start_year": 2013,
                "end_year": 2016,
                "description": "Focused on deep learning for computer vision. Thesis: 'Attention Mechanisms in Medical Image Analysis'",
            },
            {
                "degree": "M.S. in Machine Learning",
                "institution": "Carnegie Mellon University",
                "location": "Pittsburgh, PA",
                "start_year": 2011,
                "end_year": 2013,
                "description": "Specialized in statistical machine learning and natural language processing.",
            },
            {
                "degree": "B.S. in Computer Science",
                "institution": "University of California, Berkeley",
                "location": "Berkeley, CA",
                "start_year": 2007,
                "end_year": 2011,
                "description": "Minor in Mathematics. Graduated with honors.",
            },
        ],
        description="Educational background"
    )
    
    # Server Settings
    debug: bool = Field(default=False, description="Debug mode")
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Global configuration instance
config = AppConfig()