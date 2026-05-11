"message": "System active. Awaiting Human-in-the-Loop TRU."
    }

# This keeps Northflank's internal health-check green
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Matches the port 8080 we see in your logs
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
