# AI Healthcare App ![License](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to the AI Healthcare App! This application is designed to assist users with healthcare inquiries using a fine-tuned AI model. The model is powered by **Ollama** and has been fine-tuned using **Unsloth**. The frontend is built with pure HTML, CSS, and JavaScript, ensuring a lightweight and responsive user experience.


## Features
- AI-powered healthcare assistance
- Light Model
- Fine-tuned model for accurate responses


# Use on your browser ![now](http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#634FA2"><path d="m243-240-51-51 405-405H240v-72h480v480h-72v-357L243-240Z) 


## Installation Instructions

### Prerequisites
- Git
- Ollama CLI
- OS: linux (recommended for smooth installation)
- 8GB of free RAM (minimum)
- 8CPUs (minimum)


## Auto install

### Install using script

1. Run the install.py
   ```bash
   cd vitals
   python3 install.py
   ```

   
## Manual install

### For Windows

1. Clone the repository:
    ```bash
    git clone https://github.com/Aviralansh/vitals.git
    ```

2. Move into the repository directory:
    ```bash
    cd vitals
    ```

3. Download [Ollama for Windows](https://ollama.com/download/windows).

4. Download the GGUF model file:
    ```bash
    curl -L -o unsloth.F16.gguf https://huggingface.co/Aviralansh/vitals-gguf-16bit/resolve/main/unsloth.F16.gguf
    ```

5. Create the model:
    ```bash
    ollama create vitals -f ./Modelfile
    ```

6. Run a local HTTP server to view the page (you can use Python’s built-in HTTP server):
    ```bash
    python -m http.server
    ```



### For Linux

1. Clone the repository:
    ```bash
    git clone https://github.com/Aviralansh/vitals.git
    ```

2. Move into the repository directory:
    ```bash
    cd vitals
    ```

3. Download Ollama for Linux
```bash
  curl -fsSL https://ollama.com/install.sh | sh
```

4. Download the GGUF model file:
    ```bash
    curl -L -o unsloth.F16.gguf https://huggingface.co/Aviralansh/vitals-gguf-16bit/resolve/main/unsloth.F16.gguf
    ```

5. Create the model:
    ```bash
    ollama create vitals -f ./Modelfile
    ```

6. Run a local HTTP server to view the page (you can use Python’s built-in HTTP server):
    ```bash
    python3 -m http.server
    ```



### For Mac

1. Clone the repository:
    ```bash
    git clone https://github.com/Aviralansh/vitals.git
    ```
    
2. Move into the repository directory:
    ```bash
    cd vitals
    ```

3. Download [Ollama for Mac](https://ollama.com/download/mac).

4. Download the GGUF model file:
    ```bash
    curl -L -o unsloth.F16.gguf https://huggingface.co/Aviralansh/vitals-gguf-16bit/resolve/main/unsloth.F16.gguf
    ```

5. Create the model:
    ```bash
    ollama create vitals -f ./Modelfile
    ```

6. Run a local HTTP server to view the page (you can use Python’s built-in HTTP server):
    ```bash
    python3 -m http.server
    ```


# Acknowledgements
- Trained using [Unsloath](https://github.com/unslothai/unsloth)
- Running Service by [Ollama](https://github.com/ollama/ollama)
