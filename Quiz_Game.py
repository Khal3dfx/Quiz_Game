import os
import random
import json

# ---------------- FILE HANDLING ----------------
FILE_NAME = "score.json"
scores = []

def load_scores():
    """Load previous scores from JSON file."""
    global scores
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                scores = json.load(file)
            except json.JSONDecodeError:
                scores = []

def save_scores():
    """Save current scores to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(scores, file, indent=4)

# Load previous scores at the start
load_scores()

# ---------------- USER INFO ----------------
# Ask for player name
os.system('cls' if os.name == 'nt' else 'clear')  # Cross-platform clear screen
name = input("Enter your name: ")

# ---------------- QUIZ DATA ----------------
# List of quiz questions with multiple choices and correct answer key
questions = [
    {
        "q": "What is the capital of Japan?",
        "choices": {"a": "Beijing", "b": "Seoul", "c": "Tokyo"},
        "answer": "c"
    },
    {
        "q": "Which data type is used to store key-value pairs in Python?",
        "choices": {"a": "List", "b": "Dictionary", "c": "Tuple"},
        "answer": "b"
    },
    {
        "q": 'What does len("Python") return?',
        "choices": {"a": "5", "b": "6", "c": "7"},
        "answer": "b"
    }
]

# Shuffle questions for randomness
random.shuffle(questions)

# ---------------- QUIZ LOGIC ----------------
score = 0

os.system('cls' if os.name == 'nt' else 'clear')
print(f"Welcome {name} to the Quiz Game! I hope you enjoy.")
input("\nPress Enter to start the Quiz...")

# Loop through each question
for q in questions:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{q['q']}")
    for key, value in q["choices"].items():
        print(f"{key}) {value}")

    # Input validation: only a/b/c allowed
    while True:
        answer = input("Your answer (a/b/c): ").lower()
        if answer in ["a", "b", "c"]:
            break
        else:
            print("❌ Invalid input. Please enter a, b, or c.")

    # Check if answer is correct
    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}) {q['choices'][q['answer']]}")

    # Show current score after each question
    print(f"Score: {score}/{len(questions)}")
    input("\nPress Enter to continue...")

# ---------------- FINAL SCORE ----------------
os.system('cls' if os.name == 'nt' else 'clear')
print(f"\nQuiz finished! Your final score: {score}/{len(questions)}")

# Save the score as a dictionary for better structure
scores.append({
    "name": name,
    "score": score,
    "total": len(questions)
})

# Save scores to JSON file
save_scores()

print("\nThank you for playing the Quiz Game! ✅")
