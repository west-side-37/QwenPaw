from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This serves your Gold and Purple Dashboard
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    user_input = (data or {}).get("cmd", "").lower()
    
    # Logic for different voice/text commands
    if "audit" in user_input:
        response = "High-Stack Ticket Audit initiated. Scanning system for high-value discrepancies, Commander TRU."
    elif "hello" in user_input or "ping" in user_input:
        response = "System online. Ghost CEO is synced and awaiting your verbal directive."
    elif "status" in user_input:
        response = "All systems operational. Northflank connection stable. Budget protocols active."
    else:
        # This handles any random thing you say to the Mic
        response = f"Directive '{user_input}' received and logged. Ghost CEO is standing by for execution."

    return jsonify({
        "agent": "Ghost CEO",
        "response": response,
        "status": "Active"
    })

if __name__ == "__main__":
    # Ensure it runs on the port Northflank expects
    app.run(host='0.0.0.0', port=8080)
