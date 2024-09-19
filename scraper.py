from bs4 import BeautifulSoup
import requests



def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching the data: {e}")
    

    soup = BeautifulSoup(response.content, "html.parser")
    return soup



def extract_data(soup):
    paragraphs = soup.find_all('p')
    return [para.get_text() for para in  paragraphs]

