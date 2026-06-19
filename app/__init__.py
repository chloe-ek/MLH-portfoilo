import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    about = {
        "name": "Chloe",
        "bio": "Hi! I'm Chloe, a software developer and MLH Fellow based in Vancouver. I love building things for the web and learning new technologies. Outside of coding, I enjoy exploring new places and trying new foods."
    }
    experiences = [
        {
            "title": "MLH Fellow",
            "company": "MLH Fellowship (Meta Track)",
            "duration": "June 2026 - Present",
            "description": "Production Engineering Fellow working on infrastructure and site reliability."
        },
        {
            "company": "Tech Startup",
            "role": "Software Engineering Intern",
            "duration": "Sep 2024 – Dec 2025",
            "description": "Built and shipped features for the main product using React and Node.js."
        },
        {
            "company": "University Research Lab",
            "role": "Research Assistant",
            "duration": "Sep 2024 – Dec 2025",
            "description": "Assisted with data analysis and machine learning experiments."
        }
    ]
    education = [
        {
            "school": "British Columbia Institute of Technology",
            "degree": "Computer Systems Technology",
            "years": "2024 – 2025"
        }
    ]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"),
                           about=about, experiences=experiences, education=education)
