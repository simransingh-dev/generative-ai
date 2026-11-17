import numpy as np

# Possible next tokens
tokens = ["Pizza", "Burger", "Pasta", "Rice", "Salad"]

# Example logits
logits = np.array([3.0, 2.0, 1.5, 0.8, 0.2])


# 1. Softmax with temperature
def get_probabilities(logits, temperature=1.0):

    temperature = max(temperature, 1e-6)

    scaled_logits = logits / temperature

    exp_values = np.exp(
        scaled_logits - np.max(scaled_logits)
    )

    probabilities = exp_values / np.sum(exp_values)

    return probabilities


# 2. Top-K sampling
def top_k_sampling(probabilities, k=3):

    indices = np.argsort(probabilities)[-k:]

    filtered = np.zeros_like(probabilities)

    filtered[indices] = probabilities[indices]

    filtered /= filtered.sum()

    return filtered


# 3. Top-P sampling
def top_p_sampling(probabilities, p=0.90):

    sorted_indices = np.argsort(probabilities)[::-1]

    sorted_probs = probabilities[sorted_indices]

    cumulative_probs = np.cumsum(sorted_probs)

    cutoff = np.searchsorted(cumulative_probs, p) + 1

    selected_indices = sorted_indices[:cutoff]

    filtered = np.zeros_like(probabilities)

    filtered[selected_indices] = probabilities[selected_indices]

    filtered /= filtered.sum()

    return filtered


# Display results
def display_results(title, probabilities):

    print("\n" + title)

    for token, probability in zip(tokens, probabilities):

        print(f"{token:10s}: {probability:.4f}")


# Experiment 1: Temperature
for temperature in [0.2, 0.7, 1.5]:

    probabilities = get_probabilities(
        logits,
        temperature
    )

    display_results(
        f"Temperature = {temperature}",
        probabilities
    )


# Experiment 2: Top-K
base_probs = get_probabilities(logits)

top_k_probs = top_k_sampling(
    base_probs,
    k=3
)

display_results("Top-K Sampling (K=3)", top_k_probs)


top_p_probs = top_p_sampling(
    base_probs,
    p=0.90
)

display_results("Top-P Sampling (P=0.90)", top_p_probs)


selected_index = np.random.choice(
    len(tokens),
    p=top_k_probs
)

print("\nSelected next token:", tokens[selected_index])