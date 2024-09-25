from bs4 import BeautifulSoup
import requests

# Fetching data from the URL
def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error if status is not 200 OK
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching the data: {e}")
    
    # Parse the content of the web page with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# Extract data from the parsed HTML content
def extract_data(soup):
    # Find all the necessary HTML elements and extract their text

    # Extract paragraphs
    paragraphs = [para.get_text() for para in soup.find_all('p')] 
    # Extract headings
    titles = [title.get_text() for title in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])] 
    # Extract all links
    links = [a.get('href') for a in soup.find_all('a', href=True)]  
    # Extract text from all divs
    divs = [div.get_text() for div in soup.find_all('div')]  
    # Extract text from all spans
    spans = [span.get_text() for span in soup.find_all('span')]  

    # Combine everything into a structured dictionary
    data = {
        "paragraphs": paragraphs,
        "titles": titles,
        "links": links,
        "divs": divs,
        "spans": spans
    }

    return data
