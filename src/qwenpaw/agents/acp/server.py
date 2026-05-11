import os
from flask import Flask

app = Flask(__name__)

# This is the "Front Door" that stops the Bing hijacking
@app.route("/")
def home():
    return {
        "status": "online",
        "agent": "Ghost CEO",
        "brain": "Gemma 4",
        "message": "System active. Awaiting Human-in-the-Loop TRU."
    }

# Standard health check
@app.route("/health")
def health():
    return "OK", 200

# THE ENGINE: This keeps the server listening for you
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
