import json
import string
import random
import os

class URLShortener:
    def __init__(self, db_file='url_db.json'):
        self.db_file = db_file
        self.urls = self.load_db()

    def load_db(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {}

    def save_db(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.urls, f, indent=4)

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choice(characters) for _ in range(6))
            if code not in self.urls:
                return code

    def shorten(self, long_url):
        # Check if already exists
        for code, url in self.urls.items():
            if url == long_url:
                return code
        
        code = self.generate_short_code()
        self.urls[code] = long_url
        self.save_db()
        return code

    def resolve(self, short_code):
        return self.urls.get(short_code, "Code not found.")

def main():
    shortener = URLShortener()
    print("--- Python URL Shortener ---")
    while True:
        print("\n1. Shorten URL")
        print("2. Resolve Short Code")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == '1':
            url = input("Enter long URL: ")
            code = shortener.shorten(url)
            print(f"Short code: {code} (http://short.ly/{code})")
        elif choice == '2':
            code = input("Enter short code: ")
            print(f"Long URL: {shortener.resolve(code)}")
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
