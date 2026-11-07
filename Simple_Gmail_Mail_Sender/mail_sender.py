################################################################
#
# Project Name : Simple Gmail Mail Sender
# Description  : Send Emails using Python SMTP
# Language     : Python
# Author       : Nikunj Patidar
#
################################################################


################################################################
#
# Importing Required Libraries
#
################################################################

import smtplib
from email.message import EmailMessage
import os


################################################################
#
# Function Name : send_mail
# Input         : sender, app_password, receiver, subject, body
# Output        : Sends an email to the specified receiver
# Description   : Establishes a secure SMTP connection with
#                 Gmail, authenticates the sender using an
#                 app password, and sends the email message.
#
################################################################

def send_mail(sender, app_password, receiver, subject, body):

    # Step 1 : Create an EmailMessage object
    msg = EmailMessage()

    # Step 2 : Configure email headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add email body
    msg.set_content(body)

    # Step 4 : Establish a secure SMTP SSL connection
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        # Step 5 : Authenticate using Gmail App Password
        smtp.login(sender, app_password)

        # Step 6 : Send the email
        smtp.send_message(msg)


################################################################
#
# Function Name : main
# Input         : None
# Output        : Executes the email sending operation
# Description   : Retrieves credentials from environment
#                 variables, defines the email content,
#                 and calls the send_mail() function.
#
################################################################

def main():

    # Retrieve sender email and app password securely
    sender_email = os.getenv("GMAIL_ADDRESS")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    # Validate required environment variables
    if not sender_email or not app_password:
        print("Error : Gmail credentials are not configured")
        return

    # Receiver email address
    receiver_email = "receiver@example.com"

    # Email subject
    subject = "Test Mail from Python Script"

    # Email body
    body = """Hello,

This is a test email sent using Python SMTP.

Regards,
Python Automation System
"""

    # Send the email
    send_mail(sender_email, app_password, receiver_email, subject, body)

    print("Mail Sent Successfully")


################################################################
#
# Starter of the Program
#
################################################################

if __name__ == "__main__":
    main()
