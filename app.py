import sys
from configparser import ConfigParser
from chatbot import ChatBot

def main():
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = config['gemini_ai']['API_KEY']

    chatBot = ChatBot(api_key=api_key)    
    chatBot.start_conversation()
    
    print('Welcome to My Gemini AI chatbot! Type quit to exit.')

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            sys.exit("Exiting Chatbot...")
            break

        try:
            response = chatBot.send_prompt(user_input)
            print(f"{chatBot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")
        

main()
