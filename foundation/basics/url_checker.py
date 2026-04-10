import requests

url = input("Enter URL: ")
try:
    res = requests.get(url)
    print("Status Code:", res.status_code)
except:
    print("Invalid URL")
