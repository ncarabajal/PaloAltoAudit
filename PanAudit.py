import requests
import xml.etree.ElementTree as ET
import argparse
import json
import xmltodict

DEBUG = False
URL = ''
USER = ''
PASSWORD = ''

def session_key(user, password, url):
    payload = {'type': 'keygen', 'user': user, 'password': password}
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        root = ET.fromstring(r.text)
        for key in root.iter('key'):
            key = key.text
            return key
            if DEBUG:
                print(key)
    else:
        return print('failed')

def get_config(token, url):
    payload = {'type': 'config', 'action': 'show', 'key': token}
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        return(r.text)

if __name__ == "__main__":
    token = session_key(USER, PASSWORD, URL)
    config = get_config(token, URL)
    output = json.loads(json.dumps(xmltodict.parse(config), indent=4))
