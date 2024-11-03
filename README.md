# AI Healthcare App

Welcome to the AI Healthcare App! This application is designed to assist users with healthcare inquiries using a fine-tuned AI model. The model is powered by **Ollama** and has been fine-tuned using **Unsloth**. The frontend is built with pure HTML, CSS, and JavaScript, ensuring a lightweight and responsive user experience.

![AI Healthcare App] 

## Features
- AI-powered healthcare assistance
- Light Model
- Fine-tuned model for accurate responses


## Installation Instructions

### Prerequisites
- Git
- Ollama CLI

### For Windows

1. Clone the repository:
    ```bash
    git clone https://github.com/Aviralansh/vitals.git
    ```

2. Move into the repository directory:
    ```bash
    cd vitals
    ```

3. Download Ollama for Windows from the [Ollama website](https://ollama.com/download/windows).

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

3. Download Ollama for Mac from the [Ollama website](https://ollama.com/download/mac).

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

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, feel free to reach out!


