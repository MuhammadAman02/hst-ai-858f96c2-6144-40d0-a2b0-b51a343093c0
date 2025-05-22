# ML Engineer Portfolio

A professional portfolio website for Machine Learning Engineers built with Python-native web technologies.

## Features

- **Responsive Design**: Looks great on desktop, tablet, and mobile devices
- **Dark/Light Mode**: Toggle between dark and light themes
- **Project Showcase**: Highlight your ML projects with descriptions and links
- **Publications Section**: Display your research papers and academic work
- **Skills & Expertise**: Showcase your technical skills and areas of expertise
- **Work Experience & Education**: Present your professional background
- **Easy Customization**: Update your information in a single configuration file

## Prerequisites

- Python 3.9+

## Setup Instructions

1. Clone the repository (if applicable)

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Customize your portfolio:
   - Edit `app/core/config.py` to update your personal information, projects, skills, etc.
   - Add your profile picture and project images to the `app/static` directory

## Running the Application

Start the application with:

```bash
python main.py
```

The portfolio will be available at: http://localhost:8000

## Customization

### Changing Personal Information

Edit the `AppConfig` class in `app/core/config.py` to update:
- Your name, title, and contact information
- Social media links
- Biography and location

### Adding Projects

Add new projects to the `projects` list in `AppConfig`:

```python
{
    "title": "Your Project Title",
    "description": "Description of your project",
    "technologies": ["Tech1", "Tech2", "Tech3"],
    "image": "project_image.jpg",  # Add image to app/static/
    "github_url": "https://github.com/yourusername/project",
    "demo_url": "https://demo-url.com",
    "paper_url": "https://arxiv.org/abs/xxxx.xxxxx",
}
```

### Adding Publications

Add new publications to the `publications` list in `AppConfig`:

```python
{
    "title": "Your Paper Title",
    "authors": "Author1, A., Author2, B.",
    "conference": "Conference Name",
    "year": 2023,
    "url": "https://paper-url.com",
}
```

### Changing Theme Colors

Update the `theme_color` and `secondary_color` properties in `AppConfig` to change the color scheme.

## Deployment

### Fly.io Deployment

1. Install the Fly CLI
2. Initialize your app: `fly launch`
3. Deploy: `fly deploy`

### Other Deployment Options

The application can be deployed to any platform that supports Python applications, including:
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- DigitalOcean App Platform

## License

MIT