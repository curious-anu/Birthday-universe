import os
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/submit-message', methods=['POST'])
def submit_message():
    mood = request.form['mood']
    message = request.form['message']

    email_sender = os.environ.get('EMAIL_USER')
    email_password = os.environ.get('EMAIL_PASSWORD')
    email_receiver = email_sender  # you can change to another if needed

    email_subject = f"New Message from Amit 💖 [{mood}]"
    body = f"""You received a message from Amit 💌

Mood: {mood}
Message: {message}
"""

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = email_subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_sender, email_password)
            server.send_message(msg)

        print("✅ Email sent successfully")
        return "<h2>✨ Message sent to the stars…Thank you..Hope this lil gift made your birthday better!<br>With all love,<br>Mrs. Amit:3</br>You are the best!Pani pilo hehe✨</h2>"
    except Exception as e:
        print(f"❌ Email sending error: {e}")
        return "<h2>❌ There was an error sending your message. Please try again later.</h2>"


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

