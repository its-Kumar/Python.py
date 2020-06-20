import smtplib
from email.mime.text import MIMEText

body = "this is a test mail.how r you"

msg = MIMEText(body)
msg["From"] = "kumarshanu1009@gmail.com"
msg["To"] = "kumarshanu1009@gmail.com"
msg["Subject"] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login("username", "password")
server.send_message(msg)

print("Mail sent")

server.quit()
