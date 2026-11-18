questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "How many days are in a week?",
        "answer": "7"
    },
    {
        "question": "What planet do we live on?",
        "answer": "Earth"
    },
    {
        "question": "What is 5 multiplied by 6?",
        "answer": "30"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "answer": "100"
    }
]

score = 0

print("=== Factual Reliability Test ===\n")

for item in questions:
    print(item["question"])

    user_answer = input("Answer: ").strip()

    if user_answer.lower() == item["answer"].lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect.")
        print("Correct answer:", item["answer"], "\n")

print("============================")
print("Final score:", score, "/", len(questions))