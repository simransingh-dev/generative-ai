import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

print("===== AI TOKEN COUNTER =====")

while True:

    text = input("\nEnter your text: ")

    if text.lower() == "exit":
        print("Thank you!")
        break

    tokens = encoding.encode(text)

    print("\nToken count:", len(tokens))
    print("Token IDs:", tokens)
    print("Decoded text:", encoding.decode(tokens))