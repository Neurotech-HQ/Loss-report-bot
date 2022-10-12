import sys
from uuid import uuid4
from yaml import safe_load
from sarufi import Sarufi

# initialize the bot
sarufi = Sarufi("username", "password")


def create_bot():
    """
        function to create bot
    """
    return sarufi.create_bot(
        name="Loss Report Bot",
        description="A conversational chatbot for automating the process of registering lost property",
        intents=safe_load(open("data/intents.yaml")),
        flow=safe_load(open("data/flows.yaml")),
    )

def update_bot(bot_id: int):
    """
        function to update bot
    """
    return sarufi.update_bot(
        id=bot_id,
        intents=safe_load(open("data/intents.yaml")),
        flow=safe_load(open("data/flows.yaml")),
    )

def chat(bot_id: int):
    chat_id = str(uuid4())
    while True:
        message = input("Me : ")
        response = sarufi.chat(
            bot_id=bot_id,
            chat_id=chat_id,
            message=message,
            message_type="text",
        )
        print(f"Bot: {response}")


if __name__ == "__main__":
    # response = create_bot()
    response = update_bot(bot_id)
    print(response)