"message": "System active. Awaiting Human-in-the-Loop TRU."
    }

# This keeps Northflank's internal health-check green
@app.route("/health")
def health():
    return "OK", 200

# THE ENGINE: If this is missing, the code won't stay online!
if __name__ == "__main__":
    # Your logs show the app is listening on port 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
