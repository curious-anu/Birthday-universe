from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

@app.route('/submit-message', methods=['POST'])
def submit_message():
    mood = request.form['mood']
    message = request.form['message']

    email_sender = os.environ.get('EMAIL_USER')
    email_password = os.environ.get('EMAIL_PASSWORD')
    email_receiver = email_sender

    subject = f"New Message from Amit 💖 [{mood}]"
    body = f"Mood: {mood}\n\nMessage: {message}"

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_sender, email_password)
            server.send_message(msg)

        print("✅ Email sent")
        return "<h2>Thankyou so much bae, hope this lil digital gift makes your birthday better!I love you so much that not even any webapp or any words can describe it..<3..You are the bestest! ✨</h2><br>With lots of hugs and kisses,<br>Mrs.Amit<br><a href='https://t.me/curious_lil_star'>Link to Telegram</a><br><a href='/'>Go back to main page</a> <br><a href='/fromyou'>Go back to the magic page</a>"

    except Exception as e:
        print(f"❌ Error: {e}")
        return "<h2>Oops! Something went wrong. Try again later.</h2>"

@app.route('/')
def home():
    return render_template('indexxx.html')

@app.route('/fromyou')
def from_you():
    return render_template('fromyou.html')

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

