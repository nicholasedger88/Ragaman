# 🎮 Ragaman

A minimal Flask-based word game where players must unscramble a jumbled 4-letter word. Inspired by anagram puzzles and built with Python, Flask, and Bootstrap.

---

## 🧠 How It Works

- A random English word is chosen from a curated word list.
- The letters are shuffled and shown to the player.
- The player has unlimited guesses to solve it.
- Correct letters are revealed in-place after each guess.
- Guess history is displayed.
- You can refresh the game at any time to get a new word.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- Flask

Install dependencies:

```bash
pip install -r requirements.txt
```

### 🏃‍♂️ Run the app

```bash
python3 app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```
Ragaman/
├── app.py
├── google-10000-english.txt
├── requirements.txt
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── style.css (optional)
└── README.md
```

---

## ✨ Future Ideas

- Add difficulty levels (3–6 letter words)
- Limit guesses
- Show definitions or hints
- User login
