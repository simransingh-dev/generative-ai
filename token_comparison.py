import tiktoken

# Load tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

# Ten different texts
texts = [
    "Hello",
    "I love Python",
    "Artificial Intelligence is changing the world.",
    "Generative AI is amazing.",
    "I am learning how Large Language Models work.",
    "Python is a popular programming language.",
    "Machine learning helps computers identify patterns.",
    "The future of technology is full of possibilities.",
    "Tokenization converts text into smaller units.",
    "I want to become a Generative AI Engineer."
]

print("=" * 65)
print("             TOKEN COUNT COMPARISON")
print("=" * 65)

for i, text in enumerate(texts, start=1):

    tokens = encoding.encode(text)

    print(f"\nText {i}: {text}")
    print(f"Token Count: {len(tokens)}")
    print(f"Token IDs: {tokens}")

print("\n" + "=" * 65)