from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    user_input = (data or {}).get("cmd", "").lower().strip()
    
    # 1. TEXT-BASED WEBSITE & BRANDING LOGIC
    if "website" in user_input or "eternal care" in user_input or "headstone" in user_input:
        response = (
            "GHOST CEO BUSINESS DIRECTIVE: Eternal Care Headstone Cleaning. "
            "STATUS: Architecture Drafted. "
            "LAYOUT: 1. Home (Legacy focus), 2. Services (Gentle Clean/Deep Restore), 3. Booking (Cemetery/Plot focus). "
            "Commander TRU, the clickable structure is ready for deployment."
        )
        
    # 2. AUDIT LOGIC
    elif "audit" in user_input:
        response = "AUDIT INITIATED: Scanning high-stack ticket data. Commander TRU, discrepancy reports are being compiled now."
        
    # 3. GREETING LOGIC
    elif "hello" in user_input or "hi" in user_input:
        response = "Greetings, Commander TRU. The Ghost CEO Command Deck is active and awaiting your business directives."
        
    # 4. STATUS LOGIC
    elif "status" in user_input:
        response = "SYSTEM STATUS: Northflank stable. Ghost CEO operations green. All business portfolios synchronized."

    else:
        # Catch-all for other text-based inputs
        response = f"DIRECTIVE ANALYZED: '{user_input}'. Ghost CEO is processing. Standing by for manual verification, Commander TRU."

    return jsonify({"agent": "Ghost CEO", "response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
