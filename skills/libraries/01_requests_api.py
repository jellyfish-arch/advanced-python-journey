import requests

def fetch_post(post_id):
    """
    Fetches a post from JSONPlaceholder API.
    Demonstrates: status codes, JSON parsing, and error handling.
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for 4xx/5xx errors
        
        data = response.json()
        print(f"--- Post {post_id} ---")
        print(f"Title: {data.get('title')}")
        print(f"Body: {data.get('body')[:50]}...")
        
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    fetch_post(1)
