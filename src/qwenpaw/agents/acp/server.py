from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# This serves the Visual Command Dashboard
@app.route('/')
def home():
    return render_template('index.html')

# This is the "Listening" pathway for your commands
@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    user_input = (data or {}).get("cmd", "").lower()
    
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
