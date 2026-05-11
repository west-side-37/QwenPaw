def health():
    return "OK", 200

if __name__ == "__main__":
    # This matches the port 8080 from your logs
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
