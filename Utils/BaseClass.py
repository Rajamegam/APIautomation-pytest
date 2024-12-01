import requests
from Utilities.configurations import *
from Utils.log_utils import logUtils
import pandas as pd


class BaseClass:

    def __init__(self):
        self.header = {'Content-Type': 'application/json', 'prefer': 'return=representation'}
        self.URL = config()['URL']['baseURL']

    def set_auth_token(self, token):
        self.header['Authorization'] = f'Bearer {token}'

    def get(self, endpoint, params=None):
        try:
            response = requests.get(f'{self.URL}/{endpoint}', headers=self.header, params=params)
            logUtils.get_logger().info(f"URL details:{self.URL}/{endpoint}")
            # self.logger.info(f"Header details:{self.header},{self.set_cookie_token(self)},{params}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logUtils.get_logger().info(f"GET request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            logUtils.get_logger().error(f"GET request failed:{e}")
            return None

    def post(self, endpoint, payload=None, auth=None, data=None):
        try:
            response = requests.post(f'{self.URL}/{endpoint}', headers=self.header, json=payload, auth=auth, data=data)
            logUtils.get_logger().info(f"URL details:{self.URL}/{endpoint}")
            logUtils.get_logger().info(f"Header details:{self.header},{self.set_auth_token(self)}")
            logUtils.get_logger().info(f"Payload details:{payload}")
            logUtils.get_logger().info(f"status code:{response.status_code}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logUtils.get_logger().critical(f"POST request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            logUtils.get_logger().critical(f"POST request failed:{e}")
            return None

    def put(self, endpoint, payload=None, params=None, auth=None, data=None):
        try:
            response = requests.put(f'{self.URL}/{endpoint}', headers=self.header, json=payload, params=params,
                                    auth=auth, data=data)
            logUtils.get_logger().info(f"URL details:{self.URL}/{endpoint}")
            logUtils.get_logger().info(f"Header details:{self.header},{self.set_auth_token(self)}")
            # self.logger.info(f"Header details:{self.header},{self.set_cookie_token(self)}")
            logUtils.get_logger().info(f"Payload details:{payload}")
            logUtils.get_logger().info(f"status code:{response.status_code}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logUtils.get_logger().info(f"PUT request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            # self.logger.critical(f"PUT request failed{e}")
            print(f"PUT request failed{e}")
            return None

    def delete(self, endpoint):
        try:
            response = requests.delete(f'{self.URL}/{endpoint}', headers=self.header)
            logUtils.get_logger().info(f"URL details:{self.URL}/{endpoint}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logUtils.get_logger().info(f"DELETE request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            logUtils.get_logger().critical(f"DELETE request failed{e}")
            return None

    def patch(self, endpoint, payload=None):
        try:
            response = requests.patch(f'{self.URL}/{endpoint}', headers=self.header, json=payload)
            logUtils.get_logger().info(f"URL details:{self.URL}/{endpoint}")
            logUtils.get_logger().info(f"Payload details:{payload}")
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logUtils.get_logger().info(f"PATCH request failed:{e}")
            return response
        except requests.exceptions.RequestException as e:
            logUtils.get_logger().critical(f"PATCH request failed{e}")
            return None

    def read_data(self, file_path):
        data = pd.read_csv(file_path)
        return data.to_dict(orient="records")
