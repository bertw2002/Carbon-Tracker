import requests
from configparser import ConfigParser, RawConfigParser

def get_rest():
    rest_session = requests.Session()
    return rest_session