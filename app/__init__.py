import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

pages = [
    {"name": "Experience", "url": "/#experience"},
    {"name": "Education", "url": "/#education"},
    {"name": "Certifications", "url": "/#certifications"},
    {"name": "Hobbies", "url": "/hobbies"},
]

hobbies = [
    {
        "name": "Hiking",
        "image": "hiking.jpg",
        "description": "Love exploring trails and being out in nature."
    },
    {
        "name": "Baking",
        "image": "baking.jpg",
        "description": "Nothing beats the smell of freshly baked cookies!"
    },
    {
        "name": "Travel",
        "image": "travel.jpg",
        "description": "love visiting new cities, trying local food, and exploring new places."
    }
]

@app.route('/')
def index():
    about = {
        "name": "Chloe Kwon",
        "bio": "Hi! I'm Chloe, a software developer and MLH Fellow based in Vancouver. I love building things for the web and learning new technologies. Outside of coding, I enjoy exploring new places and trying new cafes."
    }
    experiences = [
        {
            "company": "Meta X MLH Fellowship",
            "role": "Production Engineering Fellow",
            "duration": "Jun 2026 – Present",
            "location": "Remote"
        },
        {
            "company": "Brats and Bavaria",
            "role": "Freelance Full-Stack Developer",
            "duration": "May 2025 – Present",
            "location": "Vancouver, BC"
        },
        {
            "company": "Byte Camp",
            "role": "Software Developer",
            "duration": "Sep 2025 – Dec 2025",
            "location": "Vancouver, BC"
        }
    ]
    education = [
        {
            "school": "British Columbia Institute of Technology (BCIT)",
            "degree": "Diploma in Computer Systems Technology",
            "years": "Jan 2024 – Dec 2025"
        }
    ]
    certifications = [
        {
            "name": "AWS Certified Solutions Architect – Associate",
            "credential": "SAA-C03",
            "issued": "Jun 2026"
        }
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"),
                           about=about, experiences=experiences, education=education,
                           certifications=certifications, 
                           hobbies=hobbies, pages=pages)

@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="Hobbies", hobbies=hobbies, pages=pages)
