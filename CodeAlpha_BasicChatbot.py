def chatbot():
    print("🤖 Chatbot: Hello! I’m your simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "hello":
            print("🤖 Chatbot: Hi there!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("🤖 Chatbot: I’m CodeAlphaBot!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("🤖 Chatbot: I didn’t understand that.")

# Run the chatbot
chatbot()
