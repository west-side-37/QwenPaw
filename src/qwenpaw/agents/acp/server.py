from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    user_input = (data or {}).get("cmd", "").lower()
    
    if "audit" in user_input:
        response = "High-Stack Ticket Audit initiated. Scanning system for high-value discrepancies, Commander TRU."
    elif "status" in user_input:
        response = "All systems operational. Northflank connection stable. Budget protocols active."
    else:
        response = f"Directive '{user_input}' received. Ghost CEO standing by."

    return jsonify({"agent": "Ghost CEO", "response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
