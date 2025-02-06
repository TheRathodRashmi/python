try:
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching

        # Exit condition
        if "exit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Greeting
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")

        # Asking about the chatbot
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")

        # Help with services
        elif "help" in user_input or "support" in user_input:
            print("Chatbot: Sure! I can assist with account information, troubleshooting, or general queries. What do you need help with?")

        # Thank you
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome! Is there anything else I can assist you with?")

        # Default response
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you please rephrase?")

except KeyboardInterrupt:
    print("\nChatbot: Exiting program. Goodbye!")
