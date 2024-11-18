import requests
import re
import base64
from bs4 import BeautifulSoup

DECODING_ALGORITHMS = {
    "base64": lambda x: base64.b64decode(x).decode('utf-8')
}

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def decode_data(data, algorithm):
    if algorithm in DECODING_ALGORITHMS:
        return DECODING_ALGORITHMS[algorithm](data)
    return None

def recognize_structured_data(data, pattern):
    matches = re.findall(pattern, data)
    return matches

def extract_data(url):
    raw_data = fetch_data(url)
    structured_data = recognize_structured_data(raw_data, r'[0-9]{16}')  # Example card pattern
    if not structured_data:
        decoded_data = decode_data(raw_data, "base64")
        structured_data = recognize_structured_data(decoded_data, r'[0-9]{16}')
    return structured_data
