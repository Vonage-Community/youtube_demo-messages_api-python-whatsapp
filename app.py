import os
from flask import Flask, request, Response
from dotenv import load_dotenv
from vonage import Vonage, Auth, HttpClientOptions
from vonage_messages import WhatsappText

# Load environment variables
load_dotenv()

APP_ID = os.getenv("VONAGE_APPLICATION_ID")
PRIVATE_KEY_PATH = os.getenv("VONAGE_PRIVATE_KEY_PATH")
SANDBOX_NUMBER = os.getenv("VONAGE_SANDBOX_NUMBER")
PORT = int(os.getenv("PORT", 3000)) 

# Create Flask app
app = Flask(__name__)

# Set up credentials
auth = Auth(application_id=APP_ID, private_key=PRIVATE_KEY_PATH)

# Set up for sandbox environment
options = HttpClientOptions(api_host="messages-sandbox.nexmo.com")

# Initialize Vonage Client
vonage_client = Vonage(auth, options)


def send_whatsapp_reply(to, message_text):
    message = WhatsappText(from_=SANDBOX_NUMBER, to=to, text=message_text)
    return vonage_client.messages.send(message)


@app.route("/inbound", methods=["POST"])
def inbound():
    data = request.get_json()
    sender = data.get("from")
    text = (data.get("text") or "").strip()

    reversed_text = text[::-1]
    reply = (
            "Thank you for your message! Here's what it looks like in reverse:\n\n"
            f"{reversed_text}"
    )
    send_whatsapp_reply(sender, reply)
    return Response(status=200)


@app.route("/status", methods=["POST"])
def status():
    return Response(status=200)


if __name__ == "__main__":
    app.run(port=PORT)
