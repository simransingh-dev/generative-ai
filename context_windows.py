import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

# Hypothetical context window
CONTEXT_LIMIT = 100

# Sample input
text = """
Large Language Models use tokenization
to process text. Context windows determine
how much token context can be handled.
""" * 10

tokens = encoding.encode(text)

print("Total input tokens:", len(tokens))
print("Context limit:", CONTEXT_LIMIT)

if len(tokens) <= CONTEXT_LIMIT:
    print("Input fits inside the context window.")
else:
    print("Input exceeds the context window.")
    print("Tokens exceeding limit:", len(tokens) - CONTEXT_LIMIT)

    # Educational example of truncating tokens
    truncated_tokens = tokens[:CONTEXT_LIMIT]

    print("Tokens after truncation:", len(truncated_tokens))