text = input("Enter a sentence: ")

# Count words
words = text.split()

# Count characters
characters = len(text)

# Estimate tokens
approx_tokens = max(1, len(text) // 4) if text else 0

print("\n--- Text Analysis ---")
print("Word count:", len(words))
print("Character count:", characters)
print("Approximate token count:", approx_tokens)