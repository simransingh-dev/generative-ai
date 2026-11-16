import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

text = "I am learning Generative AI."

tokens = encoding.encode(text)

print("Original Text:")
print(text)

print("\nToken IDs:")
print(tokens)

print("\nNumber of Tokens:")
print(len(tokens))

decoded_text = encoding.decode(tokens)

print("\nDecoded Text:")
print(decoded_text)