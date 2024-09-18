from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from scraper import fetch_data, extract_data

app = FastAPI()


@app.get('/') 
def scrape_data():
    return {'data': 'Hello! Scraping'}



class ScraperRequest(BaseModel):
    url : HttpUrl

@app.post('/scrape')
def scrape_data(request: ScraperRequest):
    try:
        soup = fetch_data(request.url)
        data = extract_data(soup)
        return {"data": data}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'An error occoured: {str(e)}')

