"message": "System active. Awaiting Human-in-the-Loop TRU."
    }

# This keeps the Northflank health-check green
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Use port 8080 to match your Northflank logs
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
