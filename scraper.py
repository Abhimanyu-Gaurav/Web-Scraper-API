from bs4 import BeautifulSoup
import requests

url = "https://timesofindia.indiatimes.com/city/delhi"

def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching the data: {e}")
    

    soup = BeautifulSoup(response.content, "html.parser")
    return soup

html_content= fetch_data(url)
print (html_content)

