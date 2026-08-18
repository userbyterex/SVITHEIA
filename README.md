# Svitheia

**Autonomous scientific discovery with causal rigor and falsification.**

Svitheia is an open-source multi-agent system that generates scientific hypotheses, designs experiments, actively tries to falsify them, and maintains a persistent knowledge graph of tested claims.

## Current Status
MVP 0.1 – Telegram bot focused on basic classical mechanics. Fully local and free (Ollama).

## How it works
1. Ask a scientific question
2. The system generates a falsifiable hypothesis
3. It designs and runs a simple experiment
4. A critic agent attempts to falsify the hypothesis
5. The knowledge graph is updated with the result

## Requirements
- Python 3.11+
- Ollama installed and running
- A Telegram bot token (free from @BotFather)

## Setup
1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your Telegram token
3. Install dependencies: `pip install -e .` or use `uv sync`
4. Make sure Ollama is running with your chosen model (`ollama pull llama3.1:8b`)
5. Start the bot: `python -m bot.main`

## Vision
Build a system that prioritizes truth-seeking, explicit falsification, and causal reasoning over fluent text generation.

## License
MIT
