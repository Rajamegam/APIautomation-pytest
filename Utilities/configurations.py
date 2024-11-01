import configparser


def config():
    config=configparser.ConfigParser()
    config.read("D:/API automation/Restful_Booker_Automation/Utilities/properties.ini")
    return config

