import smtplib
import ssl


host = "smtp.gmail.com"
port = 465
# port = 587

sender = "spammichdusack@gmail.com"
password = "xwymoplpnuckgmql"

receiver = "spammichdusack@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Mail from Python program
Hi!
How are you
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)


"""
with smtplib.SMTP(host) as server:
    server.starttls() and server.login(sender, password)
    server.sendmail(sender, receiver, message)
"""