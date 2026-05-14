import os
import time
import requests

# CONFIGURATION
COMMAND_DECK_URL = "https://your-northflank-app-url.com/command" # Replace with your actual URL
LOCAL_WORKSPACE = os.path.expanduser("~/Desktop/GhostCEO_Workspace")

# Ensure the workspace exists
if not os.path.exists(LOCAL_WORKSPACE):
    os.makedirs(LOCAL_WORKSPACE)
    print(f"[SYSTEM]: Local Workspace Created at {LOCAL_WORKSPACE}")

def execute_local_command(directive):
    """Interprets text commands into file actions"""
    cmd = directive.lower()
    
    # Example Logic: Creating a Website Folder locally
    if "deploy" in cmd and "website" in cmd:
        site_folder = os.path.join(LOCAL_WORKSPACE, "Eternal_Care_Site")
        if not os.path.exists(site_folder):
            os.makedirs(site_folder)
            # Create a basic local index file
            with open(os.path.join(site_folder, "index.txt"), "w") as f:
                f.write("Eternal Care Headstone Cleaning - Deployment Manifest Ready.")
            return f"SUCCESS: Local directory created at {site_folder}"
    
    return "Directive analyzed: No local file action required."

def poll_command_deck():
    print(f"[GHOST-CEO]: Local Agent Active. Polling Command Deck...")
    while True:
        try:
            # The Local Agent 'asks' the Cloud Brain for new instructions
            response = requests.post(COMMAND_DECK_URL, json={"cmd": "status_check"})
            if response.status_code == 200:
                data = response.json()
                instruction = data.get("response", "")
                
                # If the Cloud Brain sends a deployment command, execute it locally
                if "deployment" in instruction.lower():
                    result = execute_local_command(instruction)
                    print(f"[EXECUTION]: {result}")
                    
        except Exception as e:
            print(f"[ERROR]: Connection lost... {e}")
            
        time.sleep(10) # Polls every 10 seconds to save battery/bandwidth

if __name__ == "__main__":
    poll_command_deck()
