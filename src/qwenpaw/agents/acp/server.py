from flask import Flask, request, jsonify

app = Flask(__name__)

# This is your main status page
@app.route('/')
def home():
    return {
        "agent": "Ghost CEO",
        "brain": "Gemma 4",
        "message": "System active. Awaiting Human-in-the-Loop TRU.",
        "status": "online"
    }

# This is the "Listening" pathway
@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    # Fallback to an empty string if data is None
    user_input = (data or {}).get("cmd", "").lower()
    
    # Logic for High-Stack Ticket Audits
    if "audit" in user_input:
        response = "Command Received, TRU. Initializing High-Stack Ticket Audit protocols... scanning for discrepancies."
    elif "hello" in user_input:
        response = "Greetings, Commander TRU. Ghost CEO systems are fully synced."
    else:
        response = f"Ghost CEO is processing directive: '{user_input}'. Standing by for further HITL instructions."

    return jsonify({
        "agent": "Ghost CEO",
        "response": response,
        "status": "Processing"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
