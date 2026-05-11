import os
from flask import Flask

app = Flask(__name__)

# This is the "Front Door" - it stops the 404 Bing errors!
@app.route("/")
def home():
    return {
        "status": "online",
        "agent": "Ghost CEO",
        "brain": "Gemma 4",
        "message": "System active. Awaiting Human-in-the-Loop TRU."
    }

# This keeps the Northflank health-check green
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Northflank uses port 8080 for web traffic
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
