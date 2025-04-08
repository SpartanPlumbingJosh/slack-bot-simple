import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Simple message handler
@app.event("message")
def handle_message(body, say, logger):
    logger.info(body)
    say("I received your message!")

# Start the app
if __name__ == "__main__":
    print("⚡️ Simple Slack Bot is starting up!")
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
