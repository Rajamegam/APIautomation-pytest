import logging
import os
from datetime import datetime
import boto3


class logUtils:
    def __init__(self):
        self.S3_BUCKET_NAME = "pytestautomationlogs"
        self.LOCAL_LOG_DIR = os.path.join(os.getcwd(), "logs")
        self.LOG_FILE_NAME = f"logfile_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        self.LOCAL_LOG_FILE_PATH = "os.path.join(self.LOCAL_LOG_DIR, self.LOG_FILE_NAME)"

    @staticmethod
    def get_logger():
        logdir = os.path.join(os.getcwd(), "logs")
        log_file = os.path.join(logdir, f"logfile_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
        logger = logging.getLogger("API_logger")
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            filehandler = logging.FileHandler(log_file)
            error_log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
            filehandler.setFormatter(error_log_format)
            logger.addHandler(filehandler)

        return logger

    def upload_logs_to_s3(self):
        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name="us-east-1"
        )
        try:
            client.upload_file(self.LOCAL_LOG_FILE_PATH, self.S3_BUCKET_NAME, self.LOG_FILE_NAME)
            print(f"Log file uploaded successfully")
        except Exception as e:
            print(f"Failed to upload log file: {e}")


logs = logUtils()
logs.upload_logs_to_s3()
