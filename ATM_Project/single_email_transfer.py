#importing libraries required 

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your email"
SENDER_PASSKEY = "your passkey"


# create single sender email function

def single_email_send(to_email:str, subject:str, body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['Subject']  = subject
    msg['from'] = SENDER_EMAIL
    msg.attach(MIMEText(body,'plain'))


    #start server 
    server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL,SENDER_PASSKEY)
    server.sendmail(SENDER_EMAIL, to_email,msg.as_string())
    server.quit()
    print(f"Mail Successfully sent to {to_email}")
