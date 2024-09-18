from fastapi import FastAPI

app = FastAPI()


@app.get('/') 
def scrape_data():
    return {'data': 'Hello! Scraping'}

