import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import os

def main():
    # variables
    EMAIL_LIST = [
        "example@gmail.com", 
        #"example2@gmail.com"
    ]
    SUBJECT = "Hello Email"
    BODY = (
        "Please find attached my resume for your consideration. "
        "I am excited about the opportunity to contribute to your team "
        "and would love to discuss how my skills align with your needs.\n\n"
        "Best regards,\n"
        "Sender"
    )
    BASE_DIR = os.path.dirname(__file__)
    ATTACHMENTS = [os.path.join(BASE_DIR, "example.pdf")]
    HTML = get_html_template("example")

    # Send email
    #personal_email_send(EMAIL_LIST, SUBJECT, BODY, ATTACHMENTS, HTML)
    all_email_send(EMAIL_LIST, SUBJECT, BODY, ATTACHMENTS, HTML)

# ==================== NO NEED TO TOUCH ====================
def personal_email_send(EMAIL_LIST, SUBJECT, BODY, ATTACHMENTS=None, HTML=None):
    send_email(EMAIL_LIST[0], SUBJECT, BODY, ATTACHMENTS, HTML)
    print(f"Sent email to {EMAIL_LIST[0]}.")

def all_email_send(EMAIL_LIST, SUBJECT, BODY, ATTACHMENTS=None, HTML=None):
    for email in EMAIL_LIST:
        send_email(email, SUBJECT, BODY, ATTACHMENTS, HTML)
    
    print(f"Sent email to {len(EMAIL_LIST)} recipients.")

def send_email(to_email, SUBJECT, BODY, ATTACHMENTS=None, HTML=None):
    if ATTACHMENTS is None:
        ATTACHMENTS = []
    
    from_email = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASSCODE")

    msg = MIMEMultipart("related" if HTML else "mixed")   # Changed to 'related' for embedded images
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = SUBJECT

    if not HTML:
        msg.attach(MIMEText(BODY, "plain"))
    else:
        # Create the HTML part
        msg_alternative = MIMEMultipart('alternative')
        msg.attach(msg_alternative)
        
        # Attach Plain and HTML versions
        msg_alternative.attach(MIMEText(BODY, "plain"))
        msg_alternative.attach(MIMEText(HTML, "html"))
        
        # embed the logo if you have one
        current_dir = os.path.dirname(__file__)
        logo_path = os.path.join(current_dir, "logo.jpg")
        logo_path = os.path.abspath(logo_path)
        if os.path.exists(logo_path):
            with open(logo_path, "rb") as f:
                logo_image = MIMEImage(f.read())
                logo_image.add_header('Content-ID', '<logo_image>')  # This must match the cid: in your HTML
                logo_image.add_header('Content-Disposition', 'inline', filename="logo.png")
                msg.attach(logo_image)

    # Attach any additional files
    for file_path in ATTACHMENTS:
        with open(file_path, "rb") as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.send_message(msg)



# ============================ HTML TEMPLATES ============================
def get_html_template(name):
    """Returns the HTML template as a string with escaped CSS braces"""
    path = os.path.join(os.path.dirname(__file__), f"{name}.html")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    main()
