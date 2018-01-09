import time
import requests
from bs4 import BeautifulSoup
import sys
import re
from pprint import pprint

url = "http://quotes.toscrape.com"


def get_html(url):
    r = requests.get(url=url)
    return r.content


def get_author_url(quote, url):
    return url + quote.find("small", class_="author").find_next_sibling('a').get('href')


def get_tags_url(quote, url):
    tag_urls = []
    for i in quote.find_all("a", class_="tag"):
        tag_urls.append(url + i.get('href'))
    print(tag_urls)
    return tag_urls


def get_author(author_url, author_name):
    global unique_authors
    if author_name in unique_authors:
        return unique_authors[author_name]
    else:
        author_request = requests.get(author_url)
        author_soup = BeautifulSoup(author_request.content, "html.parser")
        author = {'url': author_url,
                  'author_title': author_soup.find('h3', {'class': "author-title"}).text,
                  'born_date': author_soup.find('span', {'class': "author-born-date"}).text,
                  'born_place': author_soup.find('span', {'class': "author-born-location"}).text,
                  'auhtor_about': author_soup.find('div', {'class': "author-description"}).text}
        unique_authors.update({author_name: author})
        return author
def get_tags(urls, tags):
    pass


def parse(html, url):
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.find_all('div', class_='quote')
    records = []

    for quote in quotes:
        records.append({
            'text': quote.find('span', class_="text").text,
            'author': get_author(get_author_url(quote, url), quote.find("small", class_="author").text),
            'tags': get_tags(get_tags_url(quote, url),quote.find("div", class_="tags"))
        })
    # pprint(records)


unique_authors = {}
unique_tags = {}


def main():
    parse(get_html(url), url)


if __name__ == '__main__':
    main()
