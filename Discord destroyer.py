import requests
import time

def ask_question(question, lower):
    print(question)
    response = input()
    if lower:
        return response.lower()
    else:
        return response

def ask_token(question):
    print(question)
    response = input()
    return response

Number = int(ask_question("The amount of tokens you would like to add and use this code With:", False))
channel_id = ask_question("Please enter the channel ID you would like to spam:", False)
Message = ask_question("Please input the message you would like the Selfbot to spam:", True)

tokens = [""]
for i in range(Number):
    token = ask_token("Please input your token:")
    tokens.append(token)
dc_tokens = ', '.join(tokens)
dc_tokens = '"' + dc_tokens + '"'
dc_tokens = dc_tokens.replace('"', '')

print(dc_tokens)

def api_msg():
    for token in tokens:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }

        payload = {
            "content": Message,
            "tts": True,
        }

        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)

        if response.status_code == 200:
            print(f"Message sent using token {token}")
        else:
            print(f"Failed to send message using token {token}. Response: {response.text}")

while True:
    api_msg()
    time.sleep(0.55)