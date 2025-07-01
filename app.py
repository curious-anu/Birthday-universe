from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/fromyou')
def from_you():
    return render_template('fromyou.html')

@app.route('/submit-message', methods=["POST"])
def submit_message():
    mood = request.form.get("mood")  
    message = request.form.get("message")
    print(f"Received mood: {mood}, message: {message}")  # Debug print
    with open("messagesfromamit.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([mood, message])
    return "<h2>✨ Thank you my genius developer..my amit uwu:3. Your message is now floating in the stars ✨</h2>"

@app.route('/')
def home():
    return render_template('indexxx.html')

@app.route('/timer')
def timer():
    return render_template('timer.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

@app.route('/letter')
def letter():
    return render_template('letter.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/cake')
def cake():
    return render_template('cake.html')

if __name__ == '__main__':
    app.run(debug=True)

