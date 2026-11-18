SYSTEM_PROMPT = "You are a friendly AI study assistant."

conversation_history = []
MAX_MESSAGES = 4

print("AI Study Assistant (Memory Simulator)")
print("Type 'exit' to stop.\n")

while True:
    user_message = input("You: ").strip()

    if user_message.lower() == "exit":
        print("AI: Goodbye!")
        break

    if not user_message:
        print("Please enter a message.")
        continue

    # Store user message
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Keep only the latest messages
    conversation_history = conversation_history[-MAX_MESSAGES:]

    print("\n--- Current Context ---")
    print("System:", SYSTEM_PROMPT)

    for message in conversation_history:
        print(message["role"], ":", message["content"])

    print()