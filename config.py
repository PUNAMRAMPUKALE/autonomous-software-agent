"""
config.py

Purpose
-------
Central configuration for the Autonomous Software Engineering Agent.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# ==========================================================
# Jira Configuration
# ==========================================================

JIRA_URL = os.getenv(
    "JIRA_URL",
    "",
)

JIRA_EMAIL = os.getenv(
    "JIRA_EMAIL",
    "",
)

JIRA_API_TOKEN = os.getenv(
    "JIRA_API_TOKEN",
    "",
)

PROJECT_KEY = os.getenv(
    "PROJECT_KEY",
    "KAN",
)

# ==========================================================
# GitHub Configuration
# ==========================================================

GITHUB_TOKEN = os.getenv(
    "GITHUB_TOKEN",
    "",
)

PROJECT_REPOSITORIES = {

    "KAN": {

        "repository": "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent",

        "branch": "main",

    }

}

# ==========================================================
# LLM Configuration
# ==========================================================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "mock",
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "",
)

ANTHROPIC_API_KEY = os.getenv(
    "ANTHROPIC_API_KEY",
    "",
)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    "",
)

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY",
    "",
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)

# ==========================================================
# Workspace Configuration
# ==========================================================

WORKSPACE = os.getenv(
    "WORKSPACE",
    "workspace",
)

DEFAULT_BRANCH = os.getenv(
    "DEFAULT_BRANCH",
    "main",
)

# ==========================================================
# Runtime Configuration
# ==========================================================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO",
)

MAX_PROMPT_LENGTH = int(
    os.getenv(
        "MAX_PROMPT_LENGTH",
        "50000",
    )
)

MAX_RESPONSE_LENGTH = int(
    os.getenv(
        "MAX_RESPONSE_LENGTH",
        "8000",
    )
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0",
    )
)

MAX_TOKENS = int(
    os.getenv(
        "MAX_TOKENS",
        "4096",
    )
)