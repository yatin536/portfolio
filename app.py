"""
Flask Web Application for Yatin Kumar Singh's Data Engineering Portfolio.
Run directly using: python app.py
"""

import json
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file, make_response
from data import PROFILE, SKILLS, EXPERIENCE, EDUCATION, PROJECTS, PIPELINE_STAGES, SITE_ARCHITECTURE

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yatin-portfolio-secret-key-2026'

MESSAGES_FILE = os.path.join(os.path.dirname(__file__), 'inquiries.json')

def save_message(data):
    messages = []
    if os.path.exists(MESSAGES_FILE):
        try:
            with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
                messages = json.load(f)
        except Exception:
            messages = []
    
    data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    messages.append(data)
    
    with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
        json.dump(messages, f, indent=2)

@app.route('/')
def index():
    return render_template(
        'index.html',
        profile=PROFILE,
        skills=SKILLS,
        experience=EXPERIENCE,
        education=EDUCATION,
        projects=PROJECTS,
        pipeline_stages=PIPELINE_STAGES,
        site_architecture=SITE_ARCHITECTURE,
        year=datetime.now().year
    )

@app.route('/resume')
def resume_view():
    return render_template(
        'resume.html',
        profile=PROFILE,
        skills=SKILLS,
        experience=EXPERIENCE,
        education=EDUCATION,
        projects=PROJECTS,
        year=datetime.now().year
    )

@app.route('/api/profile')
def api_profile():
    return jsonify(PROFILE)

@app.route('/api/skills')
def api_skills():
    return jsonify(SKILLS)

@app.route('/api/experience')
def api_experience():
    return jsonify(EXPERIENCE)

@app.route('/api/projects')
def api_projects():
    return jsonify(PROJECTS)

@app.route('/api/pipeline-stages')
def api_pipeline_stages():
    return jsonify(PIPELINE_STAGES)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json() if request.is_json else request.form.to_dict()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', 'Portfolio Inquiry').strip()
    message = data.get('message', '').strip()

    if not name or not email or not message:
        return jsonify({
            'status': 'error',
            'message': 'Please provide your name, email, and message.'
        }), 400

    save_message({
        'name': name,
        'email': email,
        'subject': subject,
        'message': message
    })

    return jsonify({
        'status': 'success',
        'message': f'Thank you {name}! Your message has been received. Yatin will connect with you soon.'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n=======================================================")
    print(">> Yatin Kumar Singh's Portfolio running live at:")
    print(f"   http://127.0.0.1:{port}")
    print("=======================================================\n")
    app.run(host='0.0.0.0', port=port, debug=True)
