import os

# We are keeping it very basic to stop the Traceback
try:
    from flask import Flask
except ImportError:
    # If Flask is missing, we will just print a clear message instead of crashing
    Flask = None

if Flask:
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return "OK", 200
else:
    print("WAITING: Flask is not installed yet.")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    if Flask:
        app.run(host="0.0.0.0", port=port)
    else:
        # This keeps the container 'alive' so it doesn't loop-crash
        import time
        while True:
            print("Server is idling... waiting for Flask.")
            time.sleep(60)
