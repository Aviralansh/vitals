import os
import subprocess
import sys
import platform
import shutil

# Clear console and initialize
clear_command = "cls" if platform.system() == "Windows" else "clear"
os.system(clear_command)
print("Starting...")

# Variables
REPO_URL = "https://github.com/Aviralansh/vitals.git"
MODEL_URL = "https://huggingface.co/Aviralansh/vitals-gguf-16bit/resolve/main/unsloth.F16.gguf"
MODEL_NAME = "unsloth.F16.gguf"

# Helper function to run commands
def run_command(command, check=True):
    result = subprocess.run(command, shell=True, check=check)
    return result.returncode == 0

# Install curl if necessary (Linux only)
if platform.system() == "Linux" and shutil.which("curl") is None:
    print("Installing curl...")
    if not run_command("sudo apt update && sudo apt install curl -y"):
        print("Failed to install curl. Please install it manually.")
        sys.exit(1)
    print("Curl installed successfully.")

# Check for Ollama installation
if shutil.which("ollama") is None:
    print("Ollama is not installed.")
    if platform.system() == "Linux":
        print("Installing Ollama on Linux...")
        if not run_command("curl -fsSL https://ollama.com/install.sh | sh"):
            print("Failed to install Ollama. Please install it manually from https://ollama.com/download.")
            sys.exit(1)
    else:
        print("Please install Ollama manually from https://ollama.com/download according to your OS.")
        sys.exit(1)

# Download the model file
print("Downloading model file...")
if not run_command(f"curl -L -o {MODEL_NAME} {MODEL_URL}"):
    print("Failed to download the model file. Check your internet connection and try again.")
    sys.exit(1)

# Create the model with Ollama
print("Creating model with Ollama...")
if not run_command(f"ollama create vitals -f ./{MODEL_NAME}"):
    print("Failed to create the model in Ollama.")
    sys.exit(1)

# Start a local HTTP server
print("Starting a local HTTP server...")
python_command = "python3 -m http.server" if platform.system() != "Windows" else "python -m http.server"
if not run_command(python_command):
    print("Failed to start the HTTP server. Please ensure Python is installed.")
    sys.exit(1)
