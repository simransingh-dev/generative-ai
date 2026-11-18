import random

responses = [
    "AI can help you learn faster.",
    "AI generates responses using learned patterns.",
    "AI can make mistakes.",
    "AI is used in many applications.",
    "LLMs predict the next token."
]

temperature = float(input("Enter temperature (0 to 2): "))

if temperature < 0 or temperature > 2:
    print("Please enter a temperature between 0 and 2.")

elif temperature < 0.5:
    # Low temperature: predictable response
    print("\nResponse:", responses[0])

elif temperature < 1.0:
    # Medium temperature: limited variation
    print("\nResponse:", random.choice(responses[:3]))

else:
    # High temperature: more varied selection
    print("\nResponse:", random.choice(responses))