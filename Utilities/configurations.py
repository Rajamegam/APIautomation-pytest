import configparser
import os


def config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "properties.ini")
    config.read(config_path)
    return config
