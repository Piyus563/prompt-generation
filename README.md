# AI Prompt Generator 🤖

A free AI-powered web app built with Flask that lets you type any prompt and get an instant, beautifully formatted AI response — no API key needed!

## Features

- ✅ **Any Prompt → AI Response** — Ask anything, get a detailed answer
- ✅ **Free & No API Key** — Powered by PollinationsAI (completely free)
- ✅ **Markdown Rendering** — Output is properly formatted with headers, code blocks, bullet points, tables
- ✅ **Syntax Highlighting** — Code blocks are highlighted by language
- ✅ **Quick Suggestion Chips** — One-click example prompts
- ✅ **Copy Button** — Copy the raw response instantly
- ✅ **Ctrl+Enter** — Submit prompt with keyboard shortcut
- ✅ **Premium Dark UI** — Glassmorphism design with smooth animations

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/Piyus563/prompt-generation.git
cd prompt-generation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Backend  | Python + Flask          |
| AI       | PollinationsAI (free)   |
| Frontend | HTML + CSS + JavaScript |
| Markdown | marked.js               |
| Syntax   | highlight.js            |

## How It Works

1. User types any prompt in the text area
2. Flask sends the prompt to PollinationsAI via HTTP POST
3. AI response is returned and rendered as formatted Markdown
4. User can copy the response or ask another question

## License

MIT License — free to use and modify.
