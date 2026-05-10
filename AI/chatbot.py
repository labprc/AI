# Install chatterbot library

# Import ChatBot class
#for google colab !pip install chatterbot
from chatterbot import ChatBot

# Import ListTrainer for training chatbot
from chatterbot.trainers import ListTrainer


# Create chatbot object
bot = ChatBot('Bot')


# Create trainer object
trainer = ListTrainer(bot)


# Train chatbot using conversation list
trainer.train([

    # Question - Answer pairs

    "Hi, can I help you",

    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",

    "Where do you operate?",
    "We operate from Singapore",

    "What payment methods do you accept?",
    "We accept debit cards and major credit cards",

    "I would like to speak to your customer service agent",
    "Please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"

])


# Additional training data
trainer.train([

    "What payment methods do you offer?",
    "We accept debit cards and major credit cards",

    "How to contact customer service agent",
    "Please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"

])


# Infinite loop for chatbot conversation
while True:

    # Take user input
    request = input("You : ")

    # Exit condition
    if request == 'OK' or request == 'ok':

        print("Bot : Bye")
        break

    else:

        # Generate chatbot response
        response = bot.get_response(request)

        # Print response
        print("Bot :", response)