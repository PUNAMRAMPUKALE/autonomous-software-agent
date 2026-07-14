from dotenv import load_dotenv
import os

load_dotenv()

print("GITHUB_TOKEN =", os.getenv("GITHUB_TOKEN"))
print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
print("SLACK_BOT_TOKEN =", os.getenv("SLACK_BOT_TOKEN"))