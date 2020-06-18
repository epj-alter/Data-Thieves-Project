import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs
import lxml
import re


def scrape_goodreads():
    """
    Scrapes the good reads website.
    Returns a DataFrame Object.
    """
    # create needed variables
    url = 'https://www.goodreads.com/book/most_read?category=all&country=all&duration=m'
    soup = bs(rq.get(url).text, "lxml")

    # scrape ranks
    ranks = [x.text for x in soup.find_all("td", "number")]

    # scrape titles
    titles = [x.text.strip().title()
              for x in soup.find_all("a", class_="bookTitle")]

    # scrape readers
    pattern = r"(\d+,\d+)"
    readers_el = soup.find_all("span", "statistic")
    readers = [''.join(re.findall(pattern, x.text)) for x in readers_el]

    # scrape authors
    authors = soup.find_all('a', "authorName")
    authors = [author.text.strip() for author in authors]

    # scrape ratings
    pattern = r"(\d\.\d{1,2})"
    ratings = ["".join(re.findall(pattern, x.text))
               for x in soup.find_all("span", "minirating")]

    # scrape n_reviews
    pattern = r"(\d+,\d+ | \d+,\d+,\d+)"
    n_reviews = ["".join(re.findall(pattern, x.text)).strip()
                 for x in soup.find_all("span", "minirating")]

    data = pd.DataFrame({
        "rank": ranks,
        "title": titles,
        "author": authors,
        "ratings": ratings,
        "reviews": n_reviews,
        "reads": readers,
    })

    data["reviews"].replace(regex=r"\,", value="", inplace=True)
    data["reads"].replace(regex=r"\,", value="", inplace=True)

    return data


def scrape_amazon():
    """
    Scrapes the Amazon website.
    Returns a DataFrame Object.
    """
    # create needed variables
    url1 = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books'
    soup = bs(rq.get(url1).text, 'lxml')

    # scrape titles
    titles = [x.a.text.strip().title()
              for x in soup.find_all("span", "zg-item")]

    # scrape ranks
    ranks = [x.text.replace("#", "")
             for x in soup.find_all("span", "zg-badge-text")]

    # scrape authors
    blacklist = ["Paperback", "Hardcover",
                 "Board book", "Mass Market Paperback"]
    authors = [x.text for x in soup.find_all(
        "div", "a-row a-size-small") if x.text not in blacklist]

    # scrape prices
    prices = [x.text.replace("$", "")
              for x in soup.find_all("span", "p13n-sc-price")]

    # scrape ratings
    ratings = [''.join(re.findall(r"(\d.\d)\sout", x.text))
               for x in soup.find_all("span", "zg-item")]

    # scrape n_reviews
    n_reviews = ["".join(re.findall(r"stars\s+(\d+\W\d+ | \d+)", x.text.strip().replace(
        "\n", " "))).strip() for x in soup.find_all("span", "zg-item")]

    data = pd.DataFrame({
        "rank": ranks,
        "title": titles,
        "author": authors,
        "ratings": ratings,
        "reviews": n_reviews,
        "price": prices, })
    data.replace("", 0, inplace=True)
    data["reviews"].replace(regex=r"\,", value="", inplace=True)
    return data


def scrape_nytimes():
    """
    Scrapes the New York Times website.
    Returns a DataFrame Object.
    """
    # create needed variables
    url = "https://www.nytimes.com/books/best-sellers/2020/06/21/"
    lasoupe = bs(rq.get(url).text, 'lxml')

    # find titles
    titles = [x.text.title() for x in lasoupe.find_all("h3", "css-i1z3c1")]

    # find authors
    authors = [re.sub("by ", "", x.text)
               for x in lasoupe.find_all("p", "css-1nxjbfc")]

    # find number of weeks in ranking
    weeks = [''.join(re.findall(r"(\d{1,4})", x.text))
             for x in lasoupe.find_all("p", "css-t7cods")]

    # find rest of the book's data
    sections = [x.text for x in lasoupe.find_all(
        "a", "css-nzgijy") for i in range(5)]
    synopsis = [x.text if x.text !=
                "" else "null" for x in lasoupe.find_all("p", "css-5yxv3r")]
    covers = [x["src"] for x in lasoupe.find_all("img", "css-35otwa")]

    # clean the data rows
    data = pd.DataFrame({
        "title": titles,
        "author": authors,
        "weeks_in_ranking": weeks,
        "synopsis": synopsis,
        "cover_url": covers,
        "common_genre": sections, })
    data.replace("", 1, inplace=True)
    data = data.drop_duplicates(subset=["title"], keep='first')
    return data
