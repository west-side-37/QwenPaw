<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GHOST CEO COMMAND DECK</title>
    <style>
        body { background-color: #000; color: #ffd700; font-family: 'Courier New', Courier, monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; text-transform: uppercase; }
        .container { border: 4px solid #4b0082; padding: 40px; background: linear-gradient(145deg, #1a0033, #000); box-shadow: 0 0 30px #4b0082; border-radius: 15px; text-align: center; width: 80%; max-width: 600px; }
        h1 { font-size: 3rem; margin-bottom: 10px; text-shadow: 2px 2px #4b0082; letter-spacing: 5px; }
        .status { color: #fff; margin-bottom: 30px; font-size: 0.9rem; border-bottom: 1px solid #4b0082; padding-bottom: 10px; }
        .controls { display: flex; gap: 20px; justify-content: center; margin-bottom: 30px; }
        button { background: transparent; border: 2px solid #ffd700; color: #ffd700; padding: 15px 25px; cursor: pointer; font-weight: bold; transition: 0.3s; }
        button:hover { background: #ffd700; color: #000; box-shadow: 0 0 15px #ffd700; }
        #mic-btn { border-color: #4b0082; color: #fff; background: #4b0082; }
        #mic-btn:hover { background: #ffd700; color: #000; border-color: #ffd700; }
        #log { width: 100%; height: 150px; background: #000; border: 1px solid #4b0082; padding: 10px; overflow-y: auto; text-align: left; font-size: 0.8rem; color: #fff; }
    </style>
</head>
<body>

    <div class="container">
        <h1>GHOST CEO</h1>
        <div class="status">SECURE CONNECTION ACTIVE | HITL: TRU</div>

        <div class="controls">
            <button onclick="addLog('SYSTEM PINGED...')">PING SYSTEM</button>
            <button id="mic-btn" onclick="startVoice()">🎤 COMMUNICATE</button>
            <button onclick="addLog('AUDIT INITIALIZED...')">RUN AUDIT</button>
        </div>

        <div id="log">Awaiting directive from Commander TRU...</div>
    </div>

    <script>
        const logBox = document.getElementById('log');

        function addLog(msg) {
            const time = new Date().toLocaleTimeString();
            logBox.innerHTML += `<div>[${time}] ${msg}</div>`;
            logBox.scrollTop = logBox.scrollHeight;
        }

        function startVoice() {
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            const micBtn = document.getElementById('mic-btn');
            
            recognition.onstart = () => {
                micBtn.innerText = "LISTENING...";
            };

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                addLog(`COMMANDER TRU: "${transcript}"`);
                
                fetch('/command', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ cmd: transcript })
                })
                .then(res => res.json())
                .then(data => {
                    addLog(`GHOST-CEO: ${data.response}`);
                });
                
                micBtn.innerText = "🎤 COMMUNICATE";
            };

            recognition.start();
        }
    </script>
</body>
</html>
