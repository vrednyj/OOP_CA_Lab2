# -------------------------------------------------------------------------------
# Name:        L00169827_Q2_File_2.py
# Project:     OOP_CA_Lab2
#
# Author:      Vitaliy Baseckas
#
# Created:     27.11.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import sys

def scrape_the_page(data):
    parsed_page = BeautifulSoup(data.text, 'html.parser')
    print("Page title: {}".format(parsed_page.title.text))
    data = parsed_page.find_all()
    print("The word 'Apache2' on this page is met {} times.".format(str(data).upper().count('APACHE2'))) #Number of Apache2 words
    _id = parsed_page.find_all(id=True)
    print("The 'id' elements in this page are met {} times.\nThey are :".format(str(_id).count('id')))# soup.find_all(id=True)

    for element in _id:
        print('\t\t{}'.format(element.get('id')))

    links = parsed_page.find_all("a")
    print("This page contains {} links.\nThey are :".format(str(links).count('href')))
    for link_element in links:
        print('\t\t{}'.format(link_element.get('href')))


if __name__ == "__main__":
    url = 'http://192.168.85.130/'
    try:
        data = requests.get(url)
    except:
        print('Please check the url you entered')
        input('Hit any key for exit...')
        sys.exit()

    if data.status_code == 200:
        print('The host {0} has responded with status: {1}'.format(url,data.status_code))
        scrape_the_page(data)
    else:
        print('The host {0} has responded with status: {1}'.format(url,data.status_code))
        input('Hit any key for exit...')
        sys.exit()