BOOKS SCRAPER (Python)

DESCRIPTION

This project scrapes book data from https://books.toscrape.com using Python.

It collects information from 50 pages (1000 books total) and saves it into a structured Excel file.

---

FEATURES

* Scrapes all catalogue pages
* Extracts:

  * Title
  * Price
  * Availability
  * Rating
  * Product link
* Cleans and processes data
* Converts rating to numeric values (1–5)
* Sorts data by rating and price
* Exports to Excel (.xlsx)
* Includes basic anti-blocking (headers + delay)

---

TECHNOLOGIES

* Python
* Requests
* BeautifulSoup
* Pandas

---

OUTPUT

The script generates an Excel file:

books.xlsx

* 1000 books
* Clean data
* Clickable links

---

HOW TO RUN

bash:

pip install requests beautifulsoup4 pandas openpyxl

python scraper.py


---

AUTHOR

Created as a practice project to learn web scraping and data processing.
