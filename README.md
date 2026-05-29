# Grok Dynamic System Prompt Builder

A clean reference implementation for building context-aware system prompts in Grok.

This package helps Grok accurately and safely answer questions about its own capabilities based on the user's current interface and enabled integrations.

## Why This Exists
Current LLMs often hallucinate their capabilities. This project provides a structured way to inject real session context into the system prompt.

## Quick Start (Web Upload)

1. Download or clone this folder.
2. Go to your GitHub repository.
3. Click **Add file** → **Upload files**.
4. Drag the entire `grok-prompt-builder` folder (or its contents) into the upload area.
5. Commit the changes.

This structure is designed for easy drag-and-drop upload via the GitHub web interface with no hidden folders.

## Project Structure

```
grok-prompt-builder/
├── grok_prompt_builder/     # Main package
├── docs/                    # Documentation
├── tests/                   # Tests
├── LICENSE
├── NOTICE
├── README.md
├── pyproject.toml
└── verify_prompt_builder.py
```

## Running Locally

```bash
pip install -e .
python -m grok_prompt_builder
pytest
python verify_prompt_builder.py
```

## License

Apache License 2.0 — see LICENSE and NOTICE files.

Copyright holder: Super Sfera LLC
