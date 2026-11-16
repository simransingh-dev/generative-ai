import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

examples = {
    "English": "I am learning artificial intelligence.",
    "Numbers": "123456789 2026 987654321",
    "Punctuation": "Hello!!! How are you???",
    "Code": "print('Hello World')",
    "Emoji": "I love coding 🚀❤️",
    "Long sentence": (
        "Large language models process text "
        "using tokenization and numerical representations."
    )
}

for category, text in examples.items():

    tokens = encoding.encode(text)

    print("\nCategory:", category)
    print("Text:", text)
    print("Token count:", len(tokens))
    print("Token IDs:", tokens)