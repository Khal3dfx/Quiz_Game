## 🎮 Quiz Game (Python)
A simple and fun multiple-choice Quiz Game written in Python.
The game loads previous scores from a JSON file, collects the player’s name, asks randomized questions, validates answers, and saves the final score for future reference.

## 📌 Features
- ✔️ Randomized quiz questions
- ✔️ User input validation (only a/b/c accepted)
- ✔️ Saves player scores in score.json
- ✔️ Clean terminal interface (auto clear screen)
- ✔️ Beginner-friendly Python code

## 🛠️ How to Run
1. Clone the repository
```bash
git clone https://github.com/Khal3dfx/Quiz_Game.git
cd Quiz_Game
```
2. Run the game
```bash
python3 Quiz_Game.py
```

## 📂 Project Structure
```bash
Quiz_Game/
│── Quiz_Game.py        # Main game script
│── score.json          # Automatically created file storing scores
│── README.md           # Project documentation
│── .gitignore          # Git ignored files
```

## 🧠 How the Game Works
1. The program loads previous scores (if any) from score.json
2. The player enters their name
3. Questions are randomized
4. The player answers using a / b / c
5. The game checks each answer and tracks the score
6. At the end, the game saves your result into score.json

## 📜 Example Gameplay
```bash
Enter your name: Khaled

Welcome Khaled to the Quiz Game! I hope you enjoy.

Press Enter to start the Quiz...

What is the capital of Japan?
a) Beijing
b) Seoul
c) Tokyo
Your answer (a/b/c): c
✅ Correct!
Score: 1/3
```

## 🗂️ Saved Score Format (score.json)
```bash
[
    {
        "name": "Khaled",
        "score": 3,
        "total": 3
    }
]
```
## 🔧 Requirements
- Python 3.6 or higher
- No external packages required.

## 🤝 Contributing
Feel free to submit pull requests if you want to:
  - Add more quiz questions
  - Improve input validation
  - Add categories or difficulty levels

## 👤 Author

Khaled Fahad Al-Hamad
