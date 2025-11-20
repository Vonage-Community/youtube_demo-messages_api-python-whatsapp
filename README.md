# Send & Receive WhatsApp Messages With Python

A simple Python example showing how to send and receive WhatsApp messages using the Vonage Messages API Sandbox.

## Prerequisites
- Python 3.8+
- Vonage API account  
- ngrok (optional)

## Setup

```bash
# Create project folder
mkdir quickstart-whatsapp-python
cd quickstart-whatsapp-python

# Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install vonage flask python-dotenv
```

## Run

```bash
# Start ngrok so Vonage can reach your webhooks
ngrok http 3000

# Update your Sandbox webhook URLs
<ngrok-forwarding-url>/inbound
<ngrok-forwarding-url>/status

# Run Python app
python3 app.py
