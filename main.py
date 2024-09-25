from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from scraper import fetch_data, extract_data

app = FastAPI()

# Test endpoint for basic functionality
@app.get('/') 
def scrape_data():
    return {'data': 'Hello! Scraping'}

# Request model for the POST request
class ScraperRequest(BaseModel):
    url: HttpUrl  # The URL to scrape from, must be a valid HTTP URL

# POST endpoint for scraping content from the given URL
@app.post('/scrape')
def scrape_data(request: ScraperRequest):
    try:
        # Fetch and extract data using the provided URL
        soup = fetch_data(request.url)
        data = extract_data(soup)
        return {"data": data}  # Return the extracted data as a dictionary
    except Exception as e:
        # Return a 500 Internal Server Error if something goes wrong
        raise HTTPException(status_code=500, detail=f'An error occurred: {str(e)}')
