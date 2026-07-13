from dotenv import load_dotenv
import os

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

PROJECT_KEY = "KAN"

PROJECT_REPOSITORIES = {
    "KAN": {
        "repository": "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent",
        "branch": "main",
    }
}