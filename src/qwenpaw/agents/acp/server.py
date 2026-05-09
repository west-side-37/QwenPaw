3. This tells Northflank the server is healthy
@app.route("/health")
def health():
    return "OK", 200

# 4. This starts the engine
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
