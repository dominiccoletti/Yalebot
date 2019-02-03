import os
import json
import re
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)
F_PATTERN = re.compile('can i get an? (.+) in the chat', flags=re.IGNORECASE | re.MULTILINE)
SUFFIX = '❤️'

@app.route("/", methods=["POST"])
def webhook():
    """
    Receive callback to URL when message is sent in the group.
    """
    # Retrieve data on that single GroupMe message.
    message = request.get_json()
    print("Message received: %s" % message)
    if message["sender_type"] != "bot":
        matches = F_PATTERN.match(message["text"])
        if matches is not None and len(matches.groups()):
            reply(matches.groups()[0] + ' ' + SUFFIX)
    if message["system"]:
        print("System message!")

    return "ok", 200

def reply(text):
    """
    Reply in chat.
    """
    url = "https://api.groupme.com/v3/bots/post"
    data = {
        "bot_id": os.environ["BOT_ID"],
        "text": text,
    }
    request = Request(url, urlencode(data).encode())
    response = urlopen(request).read().decode()
    print("Response after message send: %s" % response)
