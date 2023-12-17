from celery import shared_task
from bs4 import BeautifulSoup
from .models import Book
import requests


@shared_task
def scrape_website(url):
    """
        This Python code scrapes data from a website by iterating through the pagination and extracting
        information such as title, price, and product description from each page. It uses the requests 
        library to make HTTP requests and the BeautifulSoup library to parse HTML content. The scraped 
        data is then saved to a Book object and stored in a database.
    """

    # Pagination
    for i in range(1,51):
        final_url = url + f"catalogue/page-{str(i)}.html"

        response = requests.get(final_url)
        soup = BeautifulSoup(response.content, "html.parser")

        for link in soup.select("h3 a"):
            link = link["href"]
            final_link = "https://books.toscrape.com/catalogue/" + link
            res = requests.get(final_link)

            nestedsoup = BeautifulSoup(res.content, "html.parser")

            try:
                title = nestedsoup.select_one("div.product_main h1").text
            except:
                title = ""
            print("Title: ", title)

            try:
                price = nestedsoup.select_one("div.product_main p.price_color").text
            except:
                price = ""
            print("Price: ", price)

            try:
                product_description = nestedsoup.select_one("div#product_description ~ p").text
            except:
                product_description = ""
            print("Description: ", product_description)
            

            obj = Book()

            obj.title = title
            obj.price = price
            obj.product_description = product_description

            obj.save()

    return "Succesfully Scrape data from website"