def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi! How can I help you?")
        elif user_input == "how are you":
            print("Chatbot: I am fine. Thank you!")
        elif user_input == "what is your name":
            print("Chatbot: I am a rule-based chatbot.")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
