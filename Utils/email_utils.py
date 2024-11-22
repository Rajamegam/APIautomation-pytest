import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Utils.BaseClass import BaseClass

api_helper = BaseClass()


def send_email(sender_email, receiver_email, subject, report_path, smtp_server, smtp_port, sender_password):
    if not os.path.exists(report_path):
        api_helper.get_logger().critical(f"Report file{report_path} not found")
        return

    body = "Hi, \n\n please find the report for the automation report"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with open(report_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment;filename = {os.path.basename(report_path)}")
        msg.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
