import requests
# pyrefly: ignore [missing-import]
from bs4 import BeautifulSoup

def scrape_quotes():
    """
    Scrapes quotes from a demo website.
    Demonstrates: requests + BeautifulSoup parsing.
    """
    url = "http://quotes.toscrape.com"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quotes = soup.find_all('div', class_='quote')
        
        print(f"--- Scraping {url} ---")
        for i, quote in enumerate(quotes[:5], 1):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f"{i}. \"{text[:50]}...\" - {author}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_quotes()
