import requests
from bs4 import BeautifulSoup
import json

def scrape_headlines(url):
    """
    Scrapes headlines from a given news-like URL.
    Note: This is a template script. URL structures vary significantly.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"Fetching data from {url}...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This example looks for common header tags (h1, h2, h3)
        # In a real scenario, you'd target specific classes like 'story-heading'
        headlines = []
        for tag in ['h1', 'h2', 'h3']:
            for item in soup.find_all(tag):
                text = item.get_text().strip()
                if text and len(text) > 10:  # Filter out very short strings
                    headlines.append(text)
        
        return list(set(headlines)) # Unique headlines
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    target_url = input("Enter a URL to scrape (e.g., https://news.ycombinator.com): ").strip()
    if not target_url:
        target_url = "https://news.ycombinator.com"
        
    results = scrape_headlines(target_url)
    
    if results:
        print(f"\nFound {len(results)} potential headlines/titles:")
        for i, h in enumerate(results[:15], 1):
            print(f"{i}. {h}")
            
        # Optional: Save to JSON
        save = input("\nSave results to JSON? (y/n): ").lower()
        if save == 'y':
            with open('scraped_data.json', 'w') as f:
                json.dump(results, f, indent=4)
            print("Data saved to scraped_data.json")
    else:
        print("No headlines found. The site might be protected or use different tags.")
