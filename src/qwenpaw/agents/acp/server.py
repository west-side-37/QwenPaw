import os
from flask import Flask

app = Flask(__name__)

# This is the "Front Door" that stops the 404 Bing errors!
@app.route("/")
def home():
    return {
        "status": "online",
        "agent": "Ghost CEO",
        "brain": "Gemma 4",
        "message": "System active. Awaiting Human-in-the-Loop TRU."
    }
