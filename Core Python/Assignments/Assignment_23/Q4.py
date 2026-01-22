# Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.

quiz = [
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    }
]

score = 0

for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! Correct answer is", q["answer"])

# Final score
print("\nQuiz Completed!")
print("Your Score:", score, "/", len(quiz))
