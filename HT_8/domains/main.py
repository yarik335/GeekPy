"""
Це все записати в: JSON, XLS, TXT, CSV файли (для самих крутих в sqlite)
Також повинен бути механізм отримання інформації лише про одного або список вказаних авторів по айдішнику автора(придумайте як це зробити)
Використовувати requests+bs4 
Домашка рахується зарахованою якщо ви даєте посилання на репозиторій де є всі необходні скрипти, отримані данні + є інструкція як користуватись вашим парсером!
Завдання №2
заходите на ось цей чайт https://www.expireddomains.net/register-deleted-domains/ 
(з ним будьте обережні) вибираєте любу на ваш вибір доменну зону і парсите список  
доменів - їх там буде десятки тисяч (звичайно ураховуючи пагінацію)
вимоги аналогічні як для попередного завдання тільки просто спарсити список і 
зберегти в 4 форматах
на все про все до мого наступного заняття - нехай щастить)))"""
from pprint import pprint
import time
import json
import useragent as useragent
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


def write_to_csv(value, file_csv):
    """Recursive function that add every list and dictionary item to csv file

    Args:
        value: expecting list or dictionary
        file_csv: file where to write
    """

    if isinstance(value, list):
        for i in value:
            write_to_csv(i, file_csv)
    elif isinstance(value, dict):
        writer = csv.writer(file_csv)
        for key, d_value in value.items():  # if value is dictionary go through it
            if isinstance(d_value, list):  # if value on exact key is list
                write_to_csv(d_value, file_csv)
            elif isinstance(d_value, dict):  # if value on exact key is list
                write_to_csv(d_value, file_csv)
            else:
                try:
                    writer.writerow([key, d_value])
                except UnicodeEncodeError:  # for file opened in utf-8 this error is useless
                    writer.writerow([key, d_value])
    else:
        writer = csv.writer(file_csv)
        writer.writerow(value)


def get_page_domain_names(link):
    """Return domain name"""

    return link.text


# url = "https://member.expireddomains.net/domains/expiredcom"
# login_url = "https://www.expireddomains.net/login/"
main_url = "https://www.expireddomains.net/deleted-com-domains"
first_page = 0
next_page = 25
has_next = True
domains = []
timeout = 0
while has_next:
    query = {"start": first_page}
    time.sleep(timeout)
    try:
        r = requests.get(main_url, params=query, headers={'User-Agent': UserAgent().random})
        if r.status_code >= 400:
            raise requests.exceptions.ConnectionError
        timeout = r.elapsed.total_seconds() * 10
        page = r.text
        soup = BeautifulSoup(page, "html.parser")
        links = soup.select("a.namelinks")
        page_has_next = soup.select("a.next")
        if links and page_has_next:   #if there is no momain and page has'nt next_page button
            domains += list(map(get_page_domain_names, links))
            print(len(domains))
        else:
            has_next = False
    except requests.exceptions.ConnectionError:
        print("Connection failed!")
        break
with open("result_json.json", 'w', encoding='utf-8')as json_file:
    json.dump(domains, json_file)

with open('result_txt.txt', 'w', encoding='utf-8')as txt_file:
    for page in domains:
        for record in page:
            txt_file.write(json.dumps(record, indent=3))
            txt_file.write('\n')
            txt_file.write('\n')
            txt_file.write('\n')
with open('result_csv.csv', 'w', encoding='utf-8')as csv_file:
    for page in domains:
        write_to_csv(page, csv_file)


# with open('result_xls.xls', 'w')as xls_f:
#     df = pd.DataFrame(domains)                #throws exeption connected with xlwt module
#     df.to_excel(xls_f.name)

