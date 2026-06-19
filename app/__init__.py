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
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), about=about)
