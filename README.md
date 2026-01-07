# Gmail SMTP Email Sender (Python)

A lightweight Python utility for sending emails via Gmail SMTP with:
- Plain-text and HTML support
- Inline images (CID)
- File attachments
- Environment-based credential management

## Features
- Gmail SMTP (SSL)
- Multipart emails (text + HTML)
- Inline logo support
- Multiple recipients
- Attachment handling

##Guide:
Install necessary repos:

1. Create & activate virtual environment:
$ python3 -m venv venv
$ source venv/bin/activate

2. Installing Libraries:
$ pip install -r requirements.txt


3. Enabling SMTP Setup for own Gmail:
3-1. Enable 2-step verification on your gmail account
    1. Google Account -> security
    2.  turn on 2 step verification)

3-2. Create App password
    1. Google Account -> security
    2. Search "App Passwords"
    3. App: Mail
    4. Name it something that reminds of the app (ex: backend - smtp)
    5. copy the 16-character password, past in .env file in the same directory as this file


By now, your .env file should look like:
GMAIL_USER = "example@gmail.com"
GMAIL_PASSCODE = "exam plee pass code" #example passcode

Attach necessary files / html / logo into the repo
Final shape of the directory should be:
- Readme.md
- .env
- main.py
- example.pdf
- example.html
- logo.jpg

4. edit the EMAIL_LIST, subject & body text, and run the main.py
