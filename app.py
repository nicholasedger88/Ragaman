from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Needed for session support

# Load and filter word list
with open("google-10000-english.txt") as f:
    all_words = [line.strip().lower() for line in f]

word_list = [w for w in all_words if len(w) == 4 and w.isalpha()]

@app.route("/", methods=["GET", "POST"])
def index():
    if "target_word" not in session or request.method == "GET":
        target_word = random.choice(word_list)
        shuffled = list(target_word)
        random.shuffle(shuffled)
        session["target_word"] = target_word
        session["jumbled_word"] = ''.join(shuffled)
        session["guess_history"] = []

    target_word = session["target_word"]
    jumbled_word = session["jumbled_word"]
    guess_history = session.get("guess_history", [])

    feedback = ""

    if request.method == "POST":
        guess = request.form.get("guess", "").lower()

        if len(guess) != len(target_word):
            feedback = f"Please enter a {len(target_word)}-letter word."
        elif guess == target_word:
            feedback = "🎉 Correct! You win!"
        else:
            result = ""
            for i in range(len(target_word)):
                result += guess[i] if guess[i] == target_word[i] else "_"
            guess_history.append(result)
            session["guess_history"] = guess_history
            feedback = "Not quite, try again!"

    return render_template("index.html",
                           jumbled=jumbled_word,
                           feedback=feedback,
                           guess_history=guess_history)

@app.route("/refresh")
def refresh():
    session.clear()
    return redirect(url_for("index"))
