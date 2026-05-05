import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
}

data = []

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.find("h3").find("a")["title"]

        price = book.find("p", class_="price_color").text.strip()
        price = price.replace("Â£", "").replace("£", "")
        price = float(price)

        availability = book.find("p", class_="instock availability").get_text(
            strip=True
        )

        rating = book.find("p", class_="star-rating")["class"][1]

        link = book.find("h3").find("a")["href"]
        link = "https://books.toscrape.com/catalogue/" + link

        data.append(
            {
                "Title": title,
                "Price (£)": price,
                "Availability": availability,
                "Rating": rating,
                "URL": link,
            }
        )

    time.sleep(random.uniform(1, 2))

df = pd.DataFrame(data)

df["Rating"] = df["Rating"].map(
    {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }
)

df = df.sort_values(by=["Rating", "Price (£)"], ascending=[False, True]).reset_index(
    drop=True
)

df["Price (£)"] = df["Price (£)"].round(2)

df["URL"] = df["URL"].apply(lambda x: f'=HYPERLINK("{x}", "Open")')

df.to_excel("books.xlsx", index=False)

print(f"Saved {len(data)} books to books.xlsx")
