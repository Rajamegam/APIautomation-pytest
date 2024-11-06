import json
import logging
import os
import requests
from Utilities.configurations import *


class BaseClass:

    def __init__(self):
        self.logger = self.get_logger()
        self.header = {'Content-Type': 'application/json'}
        self.URL = config()['URL']['baseURL']

    def set_cookie_token(self, token):
        self.header['Authorization'] = f'token={token}'

    def get_logger(self):
        logger = logging.getLogger("API_logger")
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            filehandler = logging.FileHandler('D:\API automation\Restful_Booker_Automation\logs\logfile.log')
            error_log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
            filehandler.setFormatter(error_log_format)
            logger.addHandler(filehandler)

        return logger

    def get(self, endpoint, params=None):
        try:
            response = requests.get(f'{self.URL}/{endpoint}', headers=self.header, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GET request failed:{e}")
            return None

    def post(self, endpoint, payload=None):
        try:
            response = requests.post(f'{self.URL}/{endpoint}', headers=self.header, json=payload)
            self.logger.info(f"URL details:{self.URL}/{endpoint}")
            self.logger.info(f"Header details:{self.header},{self.set_cookie_token(self)}")
            self.logger.info(f"Payload details:{payload}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self.logger.critical(f"POST request failed{e}")
            return None

    def put(self, endpoint, payload=None):
        try:
            response = requests.put(f'{self.URL}/{endpoint}', headers=self.header, json=payload)
            print(f"PUT request to {self.URL}/{endpoint} with headers: {self.header}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint):
        try:
            response = requests.delete(f'{self.URL}/{endpoint}', headers=self.header)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None

    def patch(self, endpoint):
        try:
            response = requests.patch(f'{self.URL}/{endpoint}', headers=self.header)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"PATCH request failed: {e}")
            return None
