try:
    from flask import Flask
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
