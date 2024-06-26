import requests
import wget

from bs4 import BeautifulSoup as bs

def download_hostel_data():
    """
    This function downloads the hostel data as a CSV file based on the link given in the technical test.

    Returns:
    None
    """

    hostel_url = "https://www.data.gouv.fr/fr/datasets/hebergements-touristiques-classes-en-france/"

    page = requests.get(hostel_url)

    soup = bs(page.content)

    links = soup.find_all("a", attrs={"title": "Télécharger le fichier"})

    # Find the download link for our interesting data
    data_link = links[0]["href"]

    # Downloading the file using wget and storing the result in the data folder
    wget.download(data_link, "data/hostel.csv")