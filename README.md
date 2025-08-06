# 🎮 Ragaman

A minimal Flask-based word game where players must unscramble a jumbled 4-letter word. Inspired by anagram puzzles and built with Python, Flask, and Bootstrap.

---

## 🧠 How It Works

- A random 4-letter English word is chosen from a curated word list.
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

## 🌍 Deployment

You can deploy this app on:

- [Render](https://render.com/)
- [Fly.io](https://fly.io/)
- [Railway](https://railway.app/)
- Or a basic VPS / shared hosting that supports Python

Want help deploying? Just ask.

---

## ✨ Future Ideas

- Add difficulty levels (3–6 letter words)
- Limit guesses (like Wordle)
- Show definitions or hints
- User login / high score board
- "Give me a hint" button

---

## 📜 License

MIT — free to modify and share.
