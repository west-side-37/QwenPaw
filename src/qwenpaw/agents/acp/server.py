import os
import subprocess
import sys

try:
    from flask import Flask
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask

app = Flask(__name__)
