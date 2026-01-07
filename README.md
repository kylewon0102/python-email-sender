# Gmail SMTP Email Sender (Python)

A lightweight Python utility for sending emails via Gmail SMTP with:

- Plain-text and HTML support
- Inline images (CID)
- File attachments
- Environment-based credential management

---

## Features

- Gmail SMTP (SSL)
- Multipart emails (plain text + HTML)
- Inline logo support
- Multiple recipients
- Attachment handling

---

## Setup Guide

### 1. Create & Activate Virtual Environment

    python3 -m venv venv
    source venv/bin/activate

---

### 2. Install Dependencies

    pip install -r requirements.txt

---

### 3. Gmail SMTP Configuration

#### 3.1 Enable 2-Step Verification
1. Go to Google Account → Security
2. Enable 2-Step Verification

#### 3.2 Create an App Password
1. Google Account → Security
2. Search for "App passwords"
3. App: Mail
4. Name: e.g. backend-smtp
5. Copy the generated 16-character password

---

### 4. Environment Variables

Create a .env file in the project root:

    GMAIL_USER=example@gmail.com
    GMAIL_PASSCODE=your_16_character_app_password

---

## Project Structure

    gmail-smtp-email-sender/
    ├── main.py
    ├── example.pdf
    ├── example.html
    ├── logo.jpg
    ├── requirements.txt
    ├── .env
    └── README.md

---

## Usage

1. Edit the following variables in main.py:
   - EMAIL_LIST
   - SUBJECT
   - BODY

2. Run the script:

    python main.py

Emails will be sent to all recipients listed in EMAIL_LIST.

---

## Notes

- Gmail App Passwords are required
- Inline images use CID references
- Plain-text fallback is included for compatibility
- Intended for personal automation and low-volume usage
