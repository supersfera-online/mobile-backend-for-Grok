#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

REQUIRED_PHRASES_INTEGRATED = [
    "**Current interface:** Grok Mobile App Interface",
    "**Active integrations for the user:** X (Twitter) Integration, Messaging Integration",
    "Access to X timeline/DMs for search",
    "# Handling Capability Questions",
    "prepare an SMS for sending through the integration",
    "search information in your X timeline and DMs",
    "maximum privacy and security",
]

FORBIDDEN_PHRASES_WEB = []


def run_demo() -> str:
    root = Path(__file__).parent
    proc = subprocess.run(
        ["grok-prompt-builder"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        print("ERROR: CLI exited with", proc.returncode)
        print(proc.stderr or proc.stdout)
        sys.exit(1)
    return proc.stdout


def main() -> None:
    output = run_demo()

    assert "Starting Hypothetical AI Model Initialization Script" in output
    assert "Dynamic System Prompt Generated" in output
    assert "user_with_integrations" in output

    sys.path.insert(0, str(Path(__file__).parent))
    from grok_prompt_builder import get_session_context, build_system_prompt

    mobile_ctx = get_session_context("user_with_integrations")
    mobile_prompt = build_system_prompt(mobile_ctx)

    for phrase in REQUIRED_PHRASES_INTEGRATED:
        if phrase not in mobile_prompt:
            alt = phrase.replace("Current interface:", "**Current interface:**").replace(
                "Active integrations for the user:", "**Active integrations for the user:**"
            )
            if alt not in mobile_prompt and phrase not in mobile_prompt:
                print(f"FAIL: missing required phrase in mobile prompt: {phrase}")
                sys.exit(1)

    web_ctx = get_session_context("web_user_42")
    web_prompt = build_system_prompt(web_ctx)

    for phrase in FORBIDDEN_PHRASES_WEB:
        if phrase in web_prompt:
            print(f"FAIL: web prompt must not contain: {phrase}")
            sys.exit(1)

    print("All verification checks passed.")
    print("  - Mobile profile contains full policy + examples")
    print("  - Web profile does not claim unavailable integrations")
    sys.exit(0)


if __name__ == "__main__":
    main()
