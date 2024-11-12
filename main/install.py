import os
import subprocess
import sys
import platform

# Variables
REPO_URL = "https://github.com/yourusername/vitals.git"
MODEL_URL = "https://huggingface.co/Aviralansh/vitals-gguf-16bit/resolve/main/unsloth.F16.gguf"
MODEL_NAME = "unsloth.F16.gguf"
DIRECTORY_NAME = "vitals/main/"

# Helper function to run commands
def run_command(command, check=True):
    result = subprocess.run(command, shell=True, check=check)
    return result.returncode == 0

# Install curl
if platform.system() == "Linux":
    print("Installing curl...")
    os.system("sudo apt install curl")
if platform.system() == "Windows":
    print("[!] Please install curl and wget before proceeding")
else:
    pass

# Check for Ollama installation
if not run_command("command -v ollama", check=False):
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
    print("Failed to download the model file.")
    sys.exit(1)

# Create the model using Ollama
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
