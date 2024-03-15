import re
import random

responses = {
    r'hi|hello|hey': ['Hey there!', 'Hi, how can I help you?', 'Hello, whats up?'],
    r'what\'?s? your name?': ['My name is Chatty.', "I'm Chatty, nice to meet you!"],
    r'how are you?': ["I'm good, thanks for asking!", 'Doing well, thanks!', 'I\'m an AI, so I don\'t have feelings, but I\'m running smoothly.'],
    r'tell (?:me )?a joke': ['Why did the tomato turn red? Because it saw the salad dressing!', 'What do you call a fake noodle? An Impasta!'],
    r'thank(s?| you)': ['No problem!', 'You\'re very welcome!', 'Glad I could help!'],
    r'quit|bye|exit': ['See you later!', 'Bye for now!', 'Take care!'],
    r'what\'?s? the weather (like?\s?)?(?:in )?([\w\s]+)?': ['The weather in {} is sunny today!', 'I don\'t have accurate weather information for {}, but I can try to find out if you\'d like.'],
    r'(when|what)\s?(?:is|was)?\s?([\w\s]+)\s?born': ['I\'m afraid I don\'t have information about {}\'s birth date.', 'Unfortunately, I don\'t have access to biographical data like birth dates.'],
    r'what\'?s? ([\w\s]+) (mean|definition)': ['Let me look up the definition of {}...', 'Here\'s what I found for the meaning of {}:'],
    r'(.*)': ['I\'m not sure I understand. Could you rephrase your question or ask something else?', 'Hmm, I didn\'t quite get that. Could you try asking in a different way?']
}

def respond(message):
    message = message.lower()
    for pattern, response_list in responses.items():
        match = re.match(pattern, message)
        if match:
            response = random.choice(response_list)
            if '{}' in response:
                response = response.format(*match.groups())
            return response
    return 'I\'m not sure how to respond to that.'

print('Hey there, I\'m Chatty, a friendly chatbot. Type "bye" or "exit" to leave the conversation.')
while True:
    message = input('> ')
    if message.lower() in ['bye', 'exit']:
        print('Bye for now! Take care.')
        break
    else:
        print(respond(message))
