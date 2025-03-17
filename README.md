# Requirements
- Python 3
- Ollama https://ollama.com/download

# How to run

## Ollama
- Once you have ollama installed, open a terminal and install a desired model:
  - Larger version (8b) (4.9GB): `ollama pull llama3.1`
  - Smaller version (3b) (2GB): `ollama pull llama3.2`
  - Or any other version you'd like https://ollama.com/search
- Start up ollama with `ollama serve`

## Flask server w/ frontend
- Copy the repository and extract
- Open the project folder and open in terminal
- Run `python3 -m pip install requirements.txt` or `python -m pip install requirements.txt`
- Open your browser at http://localhost:3000
