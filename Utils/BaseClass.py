import requests
from Utilities.configurations import *
import pandas as pd

from Utils.log_utils import get_logger


class BaseClass:

    def __init__(self):
        self.header = {'Content-Type': 'application/json', 'prefer': 'return=representation'}
        self.URL = config()['URL']['baseURL']
        self.logger, self.log_file = get_logger()

    def set_auth_token(self, token):
        self.header['Authorization'] = f'Bearer {token}'

    def get(self, endpoint, params=None):
        try:
            response = requests.get(f'{self.URL}/{endpoint}', headers=self.header, params=params)
            self.logger.info(f"URL details:{self.URL}/{endpoint}")
            # self.logger.info(f"Header details:{self.header},{self.set_cookie_token(self)},{params}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                self.logger.info(f"GET request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GET request failed:{e}")
            return None

    def post(self, endpoint, payload=None, auth=None, data=None):
        try:
            response = requests.post(f'{self.URL}/{endpoint}', headers=self.header, json=payload, auth=auth, data=data)
            self.logger.info(f"URL details:{self.URL}/{endpoint}")
            self.logger.info(f"Header details:{self.header},{self.set_auth_token(self)}")
            self.logger.info(f"Payload details:{payload}")
            self.logger.info(f"status code:{response.status_code}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                self.logger.critical(f"POST request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.critical(f"POST request failed:{e}")
            return None

    def put(self, endpoint, payload=None, params=None, auth=None, data=None):
        try:
            response = requests.put(f'{self.URL}/{endpoint}', headers=self.header, json=payload, params=params,
                                    auth=auth, data=data)
            self.logger.info(f"URL details:{self.URL}/{endpoint}")
            self.logger.info(f"Header details:{self.header},{self.set_auth_token(self)}")
            self.logger.info(f"Payload details:{payload}")
            self.logger.info(f"status code:{response.status_code}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                self.logger.info(f"PUT request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            # self.logger.critical(f"PUT request failed{e}")
            print(f"PUT request failed{e}")
            return None

    def delete(self, endpoint):
        try:
            response = requests.delete(f'{self.URL}/{endpoint}', headers=self.header)
            self.logger.info(f"URL details:{self.URL}/{endpoint}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                self.logger.info(f"DELETE request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.critical(f"DELETE request failed{e}")
            return None

    def patch(self, endpoint, payload=None):
        try:
            response = requests.patch(f'{self.URL}/{endpoint}', headers=self.header, json=payload)
            self.logger.info(f"URL details:{self.URL}/{endpoint}")
            self.logger.info(f"Payload details:{payload}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                self.logger.info(f"PATCH request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.critical(f"PATCH request failed{e}")
            return None

    @staticmethod
    def read_data(file_path):
        try:
            # Read CSV into a DataFrame
            data = pd.read_csv(file_path)
            return data.to_dict(orient='records')
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return []
