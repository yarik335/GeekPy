import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import csv

url = "http://quotes.toscrape.com"


def get_html(url):
    r = requests.get(url=url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def write_to_csv(value, file_csv):
    if isinstance(value, list):
        for i in value:
            write_to_csv(i, file_csv)
    elif isinstance(value, dict):
        writer = csv.writer(file_csv)
        for key, d_value in value.items():
            if isinstance(d_value, list):
                write_to_csv(d_value, file_csv)
            elif isinstance(d_value, dict):
                write_to_csv(d_value, file_csv)
            else:
                try:
                    writer.writerow([key, d_value])
                except UnicodeEncodeError:
                    writer.writerow([key, d_value])

    else:
        writer = csv.writer(file_csv)
        try:
            writer.writerow(value)
        except UnicodeEncodeError:
            writer.writerow(value)


def get_author_url(quote, url):
    return url + quote.find("small", class_="author").find_next_sibling('a').get('href')


def get_author(author_url, author_name):
    global unique_authors
    global author_id
    if author_name in unique_authors:
        return unique_authors[author_name]
    else:
        author_request = requests.get(author_url)
        author_soup = BeautifulSoup(author_request.content, "html.parser")
        author = {'id': author_id,
                  'url': author_url,
                  'author_title': author_soup.find('h3', {'class': "author-title"}).text,
                  'born_date': author_soup.find('span', {'class': "author-born-date"}).text,
                  'born_place': author_soup.find('span', {'class': "author-born-location"}).text,
                  'auhtor_about': author_soup.find('div', {'class': "author-description"}).text}
        unique_authors.update({author_name: author})
        author_id = author_id + 1
        return author


def get_tag(tag_name, tag_url):
    global unique_tags
    if tag_name in unique_tags:
        return unique_tags[tag_name]
    else:
        tag_has_next = True
        tag_count_pages = 1
        tag_next_page_url = tag_url
        tag_quotes = []
        while tag_has_next:
            tag_r = requests.get(url=tag_next_page_url)
            tag_soup = BeautifulSoup(tag_r.content, "html.parser")
            for tag_quote in tag_soup.find_all("div", class_="quote"):
                tag_quotes.append({
                    "text": tag_quote.find("span", class_="text").text,
                    "author": tag_quote.find("small", class_="author").text,
                    "auhtor_url": url + tag_quote.find("small", class_="author").find_next_sibling("a").get('href')
                })
            if tag_soup.find("li", class_="next"):
                tag_has_next = True
                tag_count_pages += 1
                tag_next_page_url = url + tag_soup.find("li", class_="next").find("a").get('href')
            else:
                tag_has_next = False

        tag = {"tag_name": tag_name,
               "tag_url": tag_url,
               "tag_quotes": tag_quotes}
        unique_tags.update({tag_name: tag})
        return tag


def get_tags(div_tags):
    tags = []
    for tag_name in div_tags.find_all("a", class_="tag"):
        tags.append(get_tag(tag_name.text, url + tag_name.get('href')))
    return tags


def get_author_by_id(authors, a_id):
    for key, value in authors.items():
        if value['id'] == a_id:
            return value


def parse(soup):
    quotes_to_parse = soup.find_all('div', class_='quote')
    quotes = []
    for quote in quotes_to_parse:
        quotes.append({
            'text': quote.find('span', class_="text").text,
            'author': get_author(get_author_url(quote, url), quote.find("small", class_="author").text),
            'tags': get_tags(quote.find("div", class_="tags"))
        })
    return quotes


unique_authors = {}
unique_tags = {}
records = []
author_id = 1


def main():
    has_next = True
    count_pages = 1
    next_page_url = url
    count_id = 1
    while has_next:
        soup = get_html(next_page_url)
        records.append(parse(soup))
        if soup.find("li", class_="next"):
            has_next = True
            count_pages += 1
            next_page_url = url + soup.find("li", class_="next").find("a").get('href')
        else:
            has_next = False
    with open("result_json.json", 'w', encoding='utf-8')as json_file:
        json.dump(records, json_file)
    with open('result_xls.xls', 'w')as xls_f:
        df = pd.DataFrame(records).T
        df.to_excel(xls_f.name)
    with open('result_txt.txt', 'w', encoding='utf-8')as txt_file:
        for page in records:
            for record in page:
                txt_file.write(json.dumps(record, indent=3))
                txt_file.write('\n')
                txt_file.write('\n')
                txt_file.write('\n')
    with open('result_csv.csv', 'w', encoding='utf-8')as csv_file:
        for page in records:
            write_to_csv(page, csv_file)


if __name__ == '__main__':
    main()
