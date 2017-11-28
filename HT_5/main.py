import argparse
import csv
import datetime
import json
import logging
import os
import urllib.error
import urllib.request

from HT_5.Config import categories
from HT_5.Config import default_category
from HT_5.Config import from_date
from HT_5.Config import item_url
from HT_5.Config import list_url
from HT_5.Config import log_file_name
from HT_5.Config import report_file_name
from HT_5.Config import result_directory_name
from HT_5.Config import score


# using for create request url
def insert_dash(string, substring, index):
    return string[:index] + substring + string[index:]


# Checking if directory already exist argument=path to new folder
def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)  # Creating new folder


# setting logger object
logger = logging.getLogger("exampleApp")
logger.setLevel(logging.INFO)


# get item by it id
def get_item(url, item_id):
    url = insert_dash(url, str(item_id), url.index(".json"))
    record_response = urllib.request.urlopen(url, timeout=5)
    record_data = json.loads(record_response.read().decode("utf-8"))
    logger.info("Item received.")
    return record_data


# Checking is there result directory in working directory
ensure_dir(os.getcwd() + "/" + result_directory_name)
# Create the logging file handler
fh = logging.FileHandler(result_directory_name + '/' + log_file_name)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# Add handler to logger object
logger.addHandler(fh)

logger.info("Program started")
logger.info("Create Result folder")

# Formatting data to api Time
from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").timestamp()

# Initialize variables
data = []

# Setting argparser
parser = argparse.ArgumentParser(description='Great Description To Be Here')
parser.add_argument('category', action='store', nargs='?', const=default_category,
                    default=default_category, choices=categories, help='Category should be here')
args = parser.parse_args()
category = args.category
logger.info("Parameters accepted")

logger.info("Send categories request.")
list_url = insert_dash(list_url, category, list_url.index(".json"))
try:
    response = urllib.request.urlopen(list_url, timeout=5)
except (ValueError, RuntimeError, TypeError, NameError) as err:
    logger.error("Something went wrong.")
except (ConnectionError, urllib.error.URLError) as err:
    logger.error("Connection fails.")
    print("Connection fails.")
else:
    data = json.loads(response.read().decode("utf-8"))
    logger.info("Received list of categories.")

# Get all keys and all items
items = []
item = {}
keys = set()
for i in range(len(data)):
    logger.info("Send item request.")
    try:
        if i == 4:
            raise urllib.error.URLError("Error")
        item = get_item(item_url, data[i])
    except (urllib.error.URLError, ConnectionError) as err:
        logger.error("Connection fails.")
        print("Connection fails.")
    except (ValueError, RuntimeError, TypeError, NameError) as err:
        logger.error("Something went wrong.")
    else:
        items.append(item)
    for j in item:
        keys.add(j)
keys = list(keys)

# Sorting some of the keys to make it more readable
for i in range(len(keys)):
    if keys[i] == "time":
        keys[0], keys[i] = keys[i], keys[0]
    if keys[i] == "id":
        keys[1], keys[i] = keys[i], keys[1]
    if keys[i] == "by":
        keys[2], keys[i] = keys[i], keys[2]
    if keys[i] == "text":
        keys[len(keys) - 1], keys[i] = keys[i], keys[len(keys) - 1]

# Open or create if don't exists cvs file
with open(result_directory_name + '/' + report_file_name, 'w') as csvfile:
    logger.info("report file created.")
    writer = csv.DictWriter(csvfile, fieldnames=keys, delimiter=',')
    writer.writeheader()  # set fields names
    for i in items:
        if i['time'] >= from_date and i['score'] >= int(score):
            writer.writerow(i)
logger.info("Program ends.")
