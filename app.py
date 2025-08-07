from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Needed for session support

# Load and filter word list
with open("google-10000-english.txt") as f:
    all_words = [line.strip().lower() for line in f]

word_list = [w for w in all_words if len(w) > 4 and w.isalpha()]

HEADER_IMAGE_FOLDER = os.path.join("static", "header_images")

HEADER_IMAGES = [
    os.path.join("header_images", fname)
    for fname in os.listdir(HEADER_IMAGE_FOLDER)
    if fname.lower().endswith((".webp", ".jpg", ".jpeg", ".png"))
]


@app.route("/", methods=["GET", "POST"])
def index():
    is_correct = False  # Default at top of route

    if "target_word" not in session or request.method == "GET":
        target_word = random.choice(word_list)
        shuffled = list(target_word)
        random.shuffle(shuffled)
        session["target_word"] = target_word
        session["jumbled_word"] = ''.join(shuffled)
        session["guess_history"] = []

        # Pick and store a header image once per game
        session["header_image"] = random.choice(HEADER_IMAGES)

    target_word = session["target_word"]
    jumbled_word = session["jumbled_word"]
    guess_history = session.get("guess_history", [])
    header_image = session.get("header_image", random.choice(HEADER_IMAGES))

    feedback = ""
    if request.method == "POST":
        guess = request.form.get("guess", "").lower()

        if len(guess) != len(target_word):
            feedback = f"Please enter a {len(target_word)}-letter word."
        elif guess == target_word:
            is_correct = True

            styled = [(letter, True) for letter in guess]  # All letters are correct
            guess_history.insert(0, styled)
            session["guess_history"] = guess_history

            feedback = f"Correct! The word was: {target_word.upper()} — guessed in {len(guess_history)} tries!"
        else:
            styled = [
                (guess[i], guess[i] == target_word[i])
                for i in range(len(target_word))
            ]
            guess_history.insert(0, styled)
            session["guess_history"] = guess_history
            feedback = "Not quite, try again!"

    return render_template("index.html",
                        jumbled=jumbled_word,
                        feedback=feedback,
                        guess_history=guess_history,
                        header_image=header_image,
                        is_correct=is_correct)


@app.route("/refresh")
def refresh():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)