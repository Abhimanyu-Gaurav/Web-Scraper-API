# Web Scraper API

## Technologies Used
- **Python**: Core programming language for backend logic.
- **FastAPI**: For building a RESTful web API.
- **BeautifulSoup**: For parsing and extracting data from static HTML.
- **Requests**: For making HTTP requests to fetch web pages.
- **Swagger UI** and **Postman**: For testing and validating API requests and responses.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Key Features](#key-features)
3. [Types of Websites We Can Scrape](#types-of-websites-we-can-scrape)
4. [Installation](#installation)
5. [How to Use](#how-to-use)
6. [License](#license)

---

## Project Description

The **Web Scraper API** is a lightweight tool built with **FastAPI** for scraping web content. It allows you to extract various HTML elements (such as paragraphs, titles, links, etc.) from **static web pages** by making HTTP requests and parsing the HTML content with **BeautifulSoup**.

This tool is ideal for scraping websites where the content is directly available in the HTML source, making it easy to extract information such as articles, product descriptions, and other static content.

---

## Key Features
- **Web Scraping for Static Content:** Scrapes content from static HTML elements like paragraphs (`<p>`), links (`<a>`), divs (`<div>`), and spans (`<span>`).
- **API-based:** Users can send URLs via POST requests to extract data dynamically from various web pages.
- **Error Handling:** Provides detailed error messages when issues arise while fetching or parsing content.
- **Tested with Swagger UI and Postman:** Easily validate scraping results via Swagger UI and Postman.

---

## Types of Websites We Can Scrape

The **Web Scraper API** is designed for scraping content from **static websites** where data is readily available in the HTML structure. Here are examples of websites it works well with:

- **Blogs and News Sites:** Extract article content, headlines, and publication dates.
- **Documentation Websites:** Scrape text from user manuals, API docs, and help pages.
- **Product Pages:** Extract product names, descriptions, and prices from static e-commerce websites.
- **Research Papers or Journals:** Extract titles, abstracts, and references from academic papers that are pre-rendered in HTML.
- **Company Websites:** Scrape static information from company pages like about sections, team details, and contact information.

The tool is ideal for websites where the content is delivered without requiring JavaScript to render dynamically. For dynamic sites that require JavaScript execution, other scraping methods would be needed.

---

## Installation

1. Clone the repository:
   ```bash
   https://github.com/Abhimanyu-Gaurav/Web-Scraper-API

2. Navigate to the project directory:
   ```bash
   cd web-scraper-api

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

---

## How to Use

1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload


2. Open your browser (Safari, Chrome, Brave) and enter the URL:
   ```bash
   http://localhost:8000/docs#

3. This should display the Swagger UI for your FastAPI application.

4. Test the /scrape endpoint directly from the Swagger UI to ensure it is working and accessible.

5. Use the POST method (/scrape) and provide a JSON in the body like this:
    - Click on the "Try it out" button.
    - Provide a JSON in the request body:
    ```json
    {
        "url": "https://timesofindia.indiatimes.com/"
    }

6. Click on the "Execute" button to send the request.

7. You should see the scraped data in the response section if the request is successful.
   

### Send a POST request using API clients:
1. Using Postman:
    - Open Postman and click the "New" button to create a new request.
    - Set the request type to POST from the dropdown menu next to the URL field.
    - Enter the URL in the URL field:
      ```bash
      http://localhost:8000/scrape/

    -  Go to the "Body" tab.
        - Select the "raw" option and choose "JSON" from the dropdown.
        - Paste the following JSON into the body:
        ```json
        {
            "url": "https://timesofindia.indiatimes.com/"
        }

    - Click the "Send" button to execute the request.
    - You should see the scraped data in the response section if the request is successful. 

2. Using cURL:
- Open your terminal and run:
    ```bash
    curl -X POST "http://localhost:8000/scrape/" -H "Content-Type: application/json" -d '{"url": "https://timesofindia.indiatimes.com/"}'
    
- search: The term you want to search (e.g., business name or type).
- total: The number of listings to retrieve (if available).

---    

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---