import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from log_utils import get_logger


def get_latest_report(reports_dir):
    try:
        files = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) if f.endswith(".html")]

        if not files:
            print("No report files found in the directory.")
            return None

        latest_file = max(files, key=os.path.getmtime)
        return latest_file
    except Exception as e:
        print(f"Error while fetching the latest report: {e}")
        return None


def send_email(sender_email, receiver_email, attachments, subject, smtp_server, smtp_port,
               sender_password):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    body = "Hi, \n\nPlease find the report for the automation test execution and its corresponding log file attached."
    msg.attach(MIMEText(body, "plain"))

    with open(report_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(report_path)}")
        msg.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    reports_dir = "reports"

    report_path = get_latest_report(reports_dir)
    logger, log_file_path = get_logger()

    if report_path and log_file_path:
        send_email(
            sender_email="rajamegam.govindaraj@ideas2it.com",
            receiver_email="rajamegam7@gmail.com",
            attachments="[report_path, log_file_path]",
            subject="Automation report and Log file",
            smtp_server="smtp.gmail.com",
            smtp_port=587,
            sender_password="tgzn csuv qryq lhvy",
        )
    else:
        print("No report found. Email not sent.")
