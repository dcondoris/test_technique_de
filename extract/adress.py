import gzip
import os
import shutil

import requests
import wget

from bs4 import BeautifulSoup as bs

def download_adress_data():
    """
    This function downloads the adress data as a CSV file based on the link given in the technical test.

    Returns:
    None
    """

    adress = "https://adresse.data.gouv.fr/"

    adress_webscrap = f"{adress}data/ban/adresses/latest/csv"

    page = requests.get(adress_webscrap)

    soup = bs(page.content)

    links = soup.find_all("a")

    for link in links:
        if 'adresses-france' in link["href"]:
            wget.download(f"{adress}{link["href"]}", "data/adress.csv.gz")

    with gzip.open("data/adress.csv.gz", "rb") as f_in:
        with open("data/adresses-france.csv", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove("data/adress.csv.gz")