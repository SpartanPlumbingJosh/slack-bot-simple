import os
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
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

# Simple HTTP server for Render
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running!')

def run_http_server() :
    port = int(os.environ.get("PORT", 3000))
    httpd = HTTPServer(('0.0.0.0', port) , SimpleHTTPRequestHandler)
    print(f"HTTP server started on port {port}")
    httpd.serve_forever() 

# Start the app
if __name__ == "__main__":
    print("⚡️ Simple Slack Bot is starting up!")
    
    # Start HTTP server in a separate thread
    threading.Thread(target=run_http_server, daemon=True) .start()
    
    # Start the Slack bot
    try:
        SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
    except Exception as e:
        print(f"Error starting the bot: {e}")
        print("Please check your API tokens and try again.")
