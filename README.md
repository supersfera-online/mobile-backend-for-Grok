# Grok Dynamic System Prompt Builder

A clean, production-grade reference implementation for building **context-aware system prompts** in Grok.

This package allows Grok to accurately and safely answer capability questions based on the user's current interface and enabled integrations (e.g. "Can you read my X DMs?" or "Can you prepare an SMS for me?").

## Why This Exists

Current LLMs often hallucinate their own capabilities. This project provides a structured, policy-driven way to inject real session context (interface + integrations + permissions) into the system prompt, along with clear rules for how the model should respond.

It is based on the original design spec created for the Grok platform.

## Features

- Typed `SessionContext` model
- Dynamic system prompt generation with a rigorous 6-step capability policy
- Pluggable context providers (easy to connect to real platform data)
- Clean separation between context and prompt rendering
- Includes the exact policy rules for honest capability disclosure
- Ready to be integrated into Grok clients or backends

## Installation

```bash
pip install -e .
```

Or for development:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from grok_prompt_builder import get_session_context, build_system_prompt

# Get context for a user (in production this comes from the platform)
ctx = get_session_context("user_with_integrations")

# Generate the dynamic system prompt block
prompt = build_system_prompt(ctx)

print(prompt)
```

Run the demo:

```bash
python -m grok_prompt_builder
# or
grok-prompt-builder
```

## Project Structure

```
.
├── grok_prompt_builder/     # Main package
│   ├── __init__.py
│   ├── context.py           # SessionContext + get_session_context()
│   ├── prompt.py            # build_system_prompt() + policy
│   └── cli.py
├── tests/                   # Test suite
├── docs/                    # Integration guide + readiness docs
├── .grok/skills/            # Example Grok skill
├── pyproject.toml
└── verify_prompt_builder.py # Contract verification script
```

## Documentation

- [Integration Guide](docs/DYNAMIC_PROMPT.md) — How clients and backend should use this
- [Production Readiness Checklist](docs/PRODUCTION_READINESS_CHECKLIST.md)
- [Executive Summary](docs/PRODUCTION_READINESS_EXECUTIVE_SUMMARY.md)

## Running Tests

```bash
pytest
```

## Verification

```bash
python verify_prompt_builder.py
```

## Status

This is a high-quality **reference implementation**.

It is **not yet production-ready** for direct use inside Grok. See the [Production Readiness Checklist](docs/PRODUCTION_READINESS_CHECKLIST.md) for the full gap analysis (P0/P1/P2 items).

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

Copyright holder: **Super Sfera LLC** (see [NOTICE](NOTICE) file).

You must include the `NOTICE` file and retain copyright notices when redistributing or creating derivative works.

## Contributing

Contributions are welcome! Please open an issue first to discuss major changes.

---

Built as part of the Grok platform design work for dynamic, honest capability disclosure.
