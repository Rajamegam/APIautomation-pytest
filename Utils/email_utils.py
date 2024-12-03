import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def get_latest_file(directory, extension):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def send_email(smtp_server, smtp_port, sender_email, sender_password, to_email, report_path, log_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = "Automation report and Log file"

    body = ("Hi,\n\nPlease find the report for the automation test execution and its corresponding log file "
            "attached.\n\nThanks.")
    msg.attach(MIMEText(body, 'plain'))

    for file_path in [report_path, log_path]:
        if file_path and os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(file_path)}'
                )
                msg.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    reports_dir = "reports"
    logs_dir = "logs"

    latest_report = get_latest_file(reports_dir, ".html")
    latest_log = get_latest_file(logs_dir, ".log")

    if latest_report and latest_log:
        send_email(
            smtp_server="smtp.gmail.com",
            smtp_port=587,
            sender_email="rajamegam.govindaraj@ideas2it.com",
            sender_password="tgzn csuv qryq lhvy",
            to_email="rajamegam7@gmail.com",
            report_path=latest_report,
            log_path=latest_log
        )
    else:
        print("Report or log file not found.")
