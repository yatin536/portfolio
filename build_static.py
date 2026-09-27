"""
Static Site Builder for Yatin Kumar Singh's Portfolio.
Renders Jinja2 templates into standalone HTML files for zero-server hosting
(GitHub Pages, Vercel, Netlify, AWS S3, etc.).

Usage:
    python build_static.py
"""

import os
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from data import PROFILE, SKILLS, EXPERIENCE, EDUCATION, PROJECTS, PIPELINE_STAGES, SITE_ARCHITECTURE

def build():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(base_dir, 'dist')
    templates_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    os.makedirs(dist_dir, exist_ok=True)

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)

    context = {
        'profile': PROFILE,
        'skills': SKILLS,
        'experience': EXPERIENCE,
        'education': EDUCATION,
        'projects': PROJECTS,
        'pipeline_stages': PIPELINE_STAGES,
        'site_architecture': SITE_ARCHITECTURE,
        'year': datetime.now().year,
        'is_static': True
    }

    # Render index.html
    index_template = env.get_template('index.html')
    rendered_index = index_template.render(context)
    with open(os.path.join(dist_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(rendered_index)
    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(rendered_index)
    print("Rendered index.html (root & dist)")

    # Render resume.html
    resume_template = env.get_template('resume.html')
    rendered_resume = resume_template.render(context)
    with open(os.path.join(dist_dir, 'resume.html'), 'w', encoding='utf-8') as f:
        f.write(rendered_resume)
    with open(os.path.join(base_dir, 'resume.html'), 'w', encoding='utf-8') as f:
        f.write(rendered_resume)
    print("Rendered resume.html (root & dist)")

    # Copy static assets
    dist_static = os.path.join(dist_dir, 'static')
    if os.path.exists(dist_static):
        shutil.rmtree(dist_static)
    shutil.copytree(static_dir, dist_static)
    print(f"Copied static assets to dist/static")

    print("\nStatic build complete! Output folder: 'dist/'")
    print("You can test locally by running: python server.py")

if __name__ == '__main__':
    build()
