# LLM Battle App

A simple app that compares responses from multiple LLMs side-by-side, so you can see how different models answer the same prompt.

## Features
- Enter a prompt and get responses from multiple language models at once
- Compare outputs side-by-side to evaluate quality, tone, and accuracy
- Built with a simple, interactive UI

## Tech Stack
- Python
- OpenAI API
- Gradio (UI)

## How It Works
1. User enters a prompt
2. The app sends the prompt to multiple LLMs via API
3. Responses are displayed side-by-side for easy comparison

## Setup
```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your API key:
```
OPENAI_API_KEY=your-key-here
```

## Run
```bash
python arena_app.py
```

## Files
- `arena.py` — core logic for fetching and comparing LLM responses
- `arena_app.py` — main app / UI entry point
