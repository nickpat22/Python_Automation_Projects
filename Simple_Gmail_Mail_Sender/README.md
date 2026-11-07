# Simple Gmail Mail Sender

A Python-based email automation project that sends emails using Gmail's SMTP server and Python's built-in email handling libraries.

The project demonstrates SMTP communication, secure email authentication, message creation, and automated email delivery using Python.

## Features

- Sends emails using Gmail SMTP.
- Establishes a secure SMTP connection using SSL.
- Authenticates using Gmail App Passwords.
- Supports customizable email recipients.
- Allows customization of email subjects and message bodies.
- Uses environment variables to store sensitive credentials.
- Automatically closes the SMTP connection after sending.

## Technologies Used

- **Programming Language:** Python
- **Email Protocol:** SMTP
- **Email Server:** Gmail SMTP
- **Secure Connection:** SMTP SSL
- **Email Handling:** email.message
- **Credential Management:** Environment Variables

## Project Structure

```text
Simple_Gmail_Mail_Sender/
│
├── mail_sender.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Prerequisites

- Python 3.x
- Gmail account
- Gmail App Password
- Internet connection

**Note:** Gmail App Passwords require 2-Step Verification to be enabled on the Google Account.

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/nickpat22/Python_Automation_Projects.git
```

**2. Navigate to the project directory**

```bash
cd Python_Automation_Projects/Simple_Gmail_Mail_Sender
```

**3. Configure Gmail credentials**

Open PowerShell and execute:

```powershell
$env:GMAIL_ADDRESS = "your_email@gmail.com"
$env:GMAIL_APP_PASSWORD = "your_app_password"
```

Replace the example values with your Gmail address and newly generated App Password.

## How to Run

Execute the Python script:

```bash
python mail_sender.py
```

The program retrieves the sender credentials from environment variables, creates the email message, establishes a secure connection with Gmail SMTP, and sends the email to the configured recipient.

## Working Process

1. Retrieves Gmail credentials from environment variables.
2. Validates the availability of the required credentials.
3. Defines the sender and receiver email addresses.
4. Creates an email message using the EmailMessage class.
5. Configures the sender, receiver, and subject headers.
6. Adds the email body.
7. Establishes a secure SMTP SSL connection with Gmail.
8. Authenticates using the sender's Gmail address and App Password.
9. Sends the email using the SMTP connection.
10. Closes the SMTP connection.

## Learning Outcomes

Through this project, I explored:

- Email automation using Python.
- SMTP protocol and email communication.
- Secure SMTP connections using SSL.
- Gmail authentication using App Passwords.
- Email message creation using EmailMessage.
- Python environment variables.
- Credential management and basic security practices.
- Resource management using context managers.

## Security Note

- Never hardcode Gmail passwords or App Passwords in source code.
- Store credentials using environment variables.
- Never upload sensitive credentials to GitHub.
- Use a newly generated App Password if previous credentials have been exposed.

## Author

**Nikunj Patidar**

GitHub: [@nickpat22](https://github.com/nickpat22)

---

*This project is part of my Python Automation learning journey, focused on email communication, SMTP integration, and secure credential handling.*
