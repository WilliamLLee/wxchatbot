# chatter.py
# function: chat with robot
# author: jack-lio
# github: https://github.com/Jack-Lio
# date: 2019.12.27

from chatbot import myChatBot

def get_response(ask):
    response = myChatBot.get_response(ask)
    return response

if __name__ == "__chatter__":
    while True:
        try:
            response = myChatBot.get_response(input())
            print(response)
        except(KeyboardInterrupt, EOFError, SystemExit):
            print("Exit!")
            break
