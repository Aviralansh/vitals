<h1 style="font-size: 3em; display: inline;">VITALS</h1>
<sup style="font-size: 0.6em; color: #666;">prototype</sup>

> **Vitals Medical Assistant is a fine-tuned AI tool based on the Llama 3 model, tailored to address medical queries. Leveraging Ollama's service for AI interaction, this assistant enables users to gain health insights and assistance with medical-related questions. Designed for accessibility and user empowerment, Vitals Medical Assistant is deployable locally or on a server, aiming to make healthcare knowledge easily accessible.**

<br>

## What is Vitals?
> ### **Model's response**: 
> _I'm Vitals! I'm a friendly AI-powered healthcare assistant designed to listen to your medical concerns and provide personalized solutions._
>
> _As Vitals, my primary goal is to help you navigate the complexities of your health journey. Whether you're experiencing symptoms, managing chronic conditions, or seeking advice on preventive care, I'm here to offer guidance and support._
>
> _I'll ask you questions about your medical history, current symptoms, and any concerns you may have. Then, using my advanced algorithms and knowledge base, I'll provide tailored recommendations for:_
>
> _1. Symptom relief: Find ways to alleviate discomfort, pain, or other symptoms._
> 2. Condition management: Offer strategies for managing chronic conditions, such as diabetes, hypertension, or asthma._
> _3. Preventive care: Provide tips on maintaining a healthy lifestyle, including nutrition, exercise, and stress reduction.
> _4. Medication guidance: Help you understand medication regimens, potential side effects, and interactions with other medications._
>
> _My ultimate goal is to empower you with the knowledge and confidence to take control of your health. So, what's been going on? What brings you to Vitals today?_

<br><br>

## Features
- Easy to use
- Uses less memory
- 8 Billion+ Parameters
- Lightning fast
- Fine-tuned model for accurate responses

<br>

## Use on your browser
If I still have credits on my hosting server, you can use [VITALS](http://139.84.143.233/) now 

<br><br>

## Installation Instructions
<br>

### Prerequisites
- Git
- Ollama CLI
- OS: linux (recommended for smooth installation)
- 8GB of free RAM (minimum)
- 8CPUs (minimum)

<br>

## Auto install

### Install using script

1. Run the install.py
   ```bash
   cd vitals
   python3 install.py
   ```

<br>

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


<br>

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


<br>

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

<br><br>
# Acknowledgements
- Trained using [Unsloath](https://github.com/unslothai/unsloth)
- Running Service by [Ollama](https://github.com/ollama/ollama)

<br><br>
# License
![License](https://img.shields.io/badge/license-MIT-blue.svg)