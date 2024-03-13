from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("api_key")

search = input("Story:")

result = requests.get(f"https://newsapi.org/v2/everything?q={search}&from=2024-03-12&to=2024-03-12&language=en&sources=bbc-news&apiKey={api_key}")

info = result.json()['totalResults']
for index in range(10):
    new_info = result.json()['articles'][index]['title']
    print(new_info)
# ['articles'][0]['title']
# print(info)