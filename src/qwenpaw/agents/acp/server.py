from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This serves your gold and purple HTML file
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    # Clean the input to make sure we can read it easily
    user_input = (data or {}).get("cmd", "").lower().strip()
    
    # THE GHOST CEO COMMUNICATION LOGIC
    if "hello" in user_input or "hi" in user_input:
        response = "Greetings, Commander TRU. The Ghost CEO Command Deck is fully operational and awaiting your lead."
        
    elif "audit" in user_input:
        response = "High-Stack Ticket Audit initiated. Scanning system for high-value discrepancies, Commander TRU. Stand by for data feed."
        
    elif "status" in user_input:
        response = "All systems operational. Northflank connection stable. London cluster responding. Budget protocols active."
        
    elif "who are you" in user_input:
        response = "I am the Ghost CEO. I am the autonomous agent designed to assist Commander TRU in high-stack ticket auditing."

    elif "clear" in user_input:
        response = "Command log cleared. Systems reset to standby."

    else:
        # This catch-all makes sure it always acknowledges exactly what you said
        response = f"Directive '{user_input}' analyzed. Ghost CEO is processing. Waiting for further manual verification from Commander TRU."

    return jsonify({"agent": "Ghost CEO", "response": response})

if __name__ == "__main__":
    # Standard Northflank port and host settings
    app.run(host='0.0.0.0', port=8080)
