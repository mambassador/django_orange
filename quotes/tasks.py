from datetime import datetime

from bs4 import BeautifulSoup

from celery import shared_task

from quotes.models import Author, Quote

import requests

from users.tasks import send_notification_mail


@shared_task()
def scrape():
    """Scrapes quotes from the website.

    This task visits the website, scrapes quotes, and saves
    them in the database.

    It collects quotes from multiple pages until it has reached
    the desired count.

    If no new quotes are added, it sends a notification email
    """
    link = "https://quotes.toscrape.com/"
    r = requests.get(link + "/page/1")

    if r.status_code != 200:
        return Exception(f"Something went wrong, response status code:{r.status_code}")

    soup = BeautifulSoup(r.text, features="html.parser")
    pager = soup.find("ul", class_="pager")
    next_button = pager.find("li", class_="next")

    page_count = 0
    quotes_counter = 0

    while next_button in pager:
        r = requests.get(link + f"/page/{page_count + 1}")
        soup = BeautifulSoup(r.text, features="html.parser")
        pager = soup.find("ul", class_="pager")
        next_button = pager.find("li", class_="next")
        page_count += 1

    for page in range(page_count):
        r = requests.get(link + f"/page/{page + 1}")
        soup = BeautifulSoup(r.text, features="html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            if quotes_counter >= 5:
                break

            quote_detail = dict()
            quote_detail["text"] = quote.find("span", class_="text").text[1:-1]

            if Quote.objects.filter(text=quote_detail["text"]).exists():
                continue

            author_link = quote.find("a")["href"]
            author_detail = get_author_detail(author_link)

            author, created = Author.objects.get_or_create(full_name=author_detail["name"])
            if created:
                author.full_name = author_detail["name"]
                author.date_of_birth = author_detail["date_of_birth"]
                author.city_of_birth = author_detail["city_of_birth"]
                author.country_of_birth = author_detail["country_of_birth"]
                author.description = author_detail["description"]
                author.save()

            quote_obj = Quote(text=quote_detail["text"], author=author)
            quote_obj.save()

            quotes_counter += 1

    if quotes_counter == 0:
        send_notification_mail(
            ["noreply@mail.com"],
            "All quotes are scraped, waiting for new quotes",
            subject="Job done",
        )


def get_author_detail(author_link):
    """Returns author details from the author's page

    Args:
        author_link (str): The relative URL of the author's page

    Returns:
        author_detail(dict): a dictionary containing the author details
    """
    author_detail = {}

    r = requests.get("https://quotes.toscrape.com/" + author_link)
    soup = BeautifulSoup(r.text, features="html.parser")

    author_detail["name"] = soup.find("h3").text

    author_detail["description"] = soup.find("div", class_="author-description").get_text(strip=True)

    date_string = soup.find("span", class_="author-born-date").text
    date_object = datetime.strptime(date_string, "%B %d, %Y")
    author_detail["date_of_birth"] = (
        date_object.year,
        date_object.month,
        date_object.day,
    )

    place_of_birth = soup.find("span", class_="author-born-location").get_text().split(",")
    if len(place_of_birth) > 1:
        author_detail["city_of_birth"] = place_of_birth[0][3:]
        author_detail["country_of_birth"] = place_of_birth[-1][1:]
    else:
        author_detail["city_of_birth"] = None
        author_detail["country_of_birth"] = place_of_birth[0][3:]

    return author_detail


if __name__ == "__main__":
    scrape()
