import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data from {url}, status code: {response.status_code}")

def parse_html(html_content, css_selector):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.select(css_selector)
    return elements

def validate_recency(date_str, date_format="%Y-%m-%d", max_days_old=30):
    data_date = datetime.strptime(date_str, date_format)
    current_date = datetime.now()
    delta = current_date - data_date
    return delta.days <= max_days_old

def extract_data(elements):
    data = []
    for element in elements:
        text = element.get_text(strip=True)
        data.append(text)
    return data

def validate_format(data, pattern):
    regex = re.compile(pattern)
    return all(regex.match(item) for item in data)

def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=["Extracted Data"])
    df.to_csv(filename, index=False)

def retrieve_data(url, css_selector, date_selector, date_format, data_pattern, output_filename):
    html_content = fetch_html(url)
    elements = parse_html(html_content, css_selector)
    date_elements = parse_html(html_content, date_selector)
    
    if not all(validate_recency(date.get_text(strip=True), date_format) for date in date_elements):
        raise Exception("Data is not recent enough")
    
    data = extract_data(elements)
    
    if not validate_format(data, data_pattern):
        raise Exception("Data format validation failed")
    
    save_to_csv(data, output_filename)
    return data
