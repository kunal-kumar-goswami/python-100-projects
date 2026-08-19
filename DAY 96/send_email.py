import os
import smtplib
import ssl
from email.mime.text import MIMEText


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.environ["GMAIL_ADDRESS"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    receiver = os.environ.get("RECEIVER_EMAIL", username)

    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = "Tesla News Update"
    msg["From"] = username
    msg["To"] = receiver

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())