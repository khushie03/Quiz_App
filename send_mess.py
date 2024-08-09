import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
import os

EMAIL_SERVER = "smtp.gmail.com"
PORT = 465
SENDER_EMAIL = "khushi2003p@gmail.com"
PASSWORD_EMAIL = "oora cvcr sjjd upgb"

def send_message(name, receiver_email):
    msg = MIMEMultipart()
    msg["Subject"] = "QUIZ Result"
    msg["From"] = formataddr(("AI Quizer", SENDER_EMAIL))
    msg["To"] = receiver_email
    msg["BCC"] = SENDER_EMAIL

    body = f"""
    Hey there, {name}!

    Thankyou for visiting our site.
    Here are the result of the exam given by you .
    You can Find the study material and the score result in the attached pdf Below .
    Welcome back to the cosmos, {name}! We can't wait to embark on this cosmic journey with you once again.
    """
    msg.attach(MIMEText(body, "plain"))

    image_path = os.path.join(os.path.dirname(__file__), 'static', 'Untitled design (1).png')

    try:
        with open(image_path, "rb") as img_file:
            img_data = img_file.read()
            img_mime = MIMEImage(img_data)
            img_mime.add_header("Content-Disposition", "attachment", filename="WelcomeBack.png")
            msg.attach(img_mime)
    except Exception as e:
        print(f"Error opening image file: {e}")

    try:
        with smtplib.SMTP_SSL(EMAIL_SERVER, PORT) as server:
            server.login(SENDER_EMAIL, PASSWORD_EMAIL)
            server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
            print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Error sending email: {e}")