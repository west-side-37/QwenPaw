app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Tells Northflank which port to use
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
