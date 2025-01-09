chatbot_active = True

responses = [
    "I am great, thank you!"
    "You are doing great, keep it up!"
    "I know right!"
    "KO, is amazing"
]
print(" Hello my dude, hows it going? ")

while chatbot_active:
    user_input = input("You: ")
    if user_input == "bye":
        print("Chatbot: Good bye and have an amazing day")
    chatbot_active = False
else:
    print("Chatbot: ", random.choice(responses))
