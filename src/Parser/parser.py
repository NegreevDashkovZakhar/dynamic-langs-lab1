from bs4 import BeautifulSoup
import requests
from Parser.model.property import Property


def parse():
    url = 'https://omsk.mlsn.ru/pokupka-nedvizhimost/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    all_rooms_count = soup.findAll("div", {"class": "content-container"})
    all_prices = soup.findAll("div", {"class": "property__price"})
    all_addresses = soup.findAll("div", {"class": "property__address"})
    all_areas = soup.findAll("div", {"class": "property__area"})
    all_descriptions = soup.findAll("div", {"class": "property__description"})
    all_properties = []
    for i in range(len(all_rooms_count)):
        current_property = Property()
        current_property.set_rooms_count(all_rooms_count[i])
        current_property.set_price(all_prices[i])
        current_property.set_address(all_addresses[i])
        current_property.set_area(all_areas[i])
        current_property.set_description(all_descriptions[i])
        all_properties.append(current_property)

    return all_properties
