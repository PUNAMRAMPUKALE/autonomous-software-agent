"""
tools/slack_tool.py
"""

import os

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()


class SlackTool:

    def __init__(self):

        token = os.getenv("SLACK_BOT_TOKEN")

        if not token:

            raise ValueError(
                "SLACK_BOT_TOKEN not configured."
            )

        self.channel = os.getenv(
            "SLACK_CHANNEL",
            "general",
        )

        self.client = WebClient(
            token=token
        )

    # ---------------------------------------------------------

    def send_message(
        self,
        message,
    ):

        print()

        print("=" * 70)
        print("SLACK TOOL")
        print("=" * 70)

        try:

            response = self.client.chat_postMessage(

                channel=self.channel,

                text=message,

            )

            print()

            print("Slack message sent.")

            return response

        except SlackApiError as ex:

            print(ex.response["error"])

            raise