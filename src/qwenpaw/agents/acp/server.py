}

# Standard health check for Northflank
@app.route("/health")
def health():
    return "OK", 200

# THE ENGINE: If this is missing, the code won't run!
if __name__ == "__main__":
    # Northflank uses port 8080 or 5000; your logs showed 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
