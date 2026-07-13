"""
config.py

Milestone 10
Global Configuration
"""

import os

from dotenv import load_dotenv

load_dotenv()

# ==========================================================
# Jira
# ==========================================================

JIRA_URL = os.getenv(
    "JIRA_URL"
)

JIRA_EMAIL = os.getenv(
    "JIRA_EMAIL"
)

JIRA_API_TOKEN = os.getenv(
    "JIRA_API_TOKEN"
)

PROJECT_KEY = os.getenv(
    "PROJECT_KEY",
    "KAN",
)

# ==========================================================
# LLM
# ==========================================================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "openai",
).lower()

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "gpt-4.1-mini",
)

# ==========================================================
# API Keys
# ==========================================================

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

ANTHROPIC_API_KEY = os.getenv(
    "ANTHROPIC_API_KEY"
)

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)

# ==========================================================
# GitHub
# ==========================================================

GITHUB_TOKEN = os.getenv(
    "GITHUB_TOKEN"
)

# ==========================================================
# Slack
# ==========================================================

SLACK_BOT_TOKEN = os.getenv(
    "SLACK_BOT_TOKEN"
)

SLACK_CHANNEL = os.getenv(
    "SLACK_CHANNEL",
    "#general",
)

# ==========================================================
# Repository Mapping
# ==========================================================

PROJECT_REPOSITORIES = {

    "KAN": {

        "repository": "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent",

        "branch": "main",

    }

}