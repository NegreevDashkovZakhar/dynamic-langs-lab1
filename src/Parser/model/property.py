from bs4 import PageElement


class Property(object):
    def __init__(self):
        self.rooms_count = None

    def set_rooms_count(self, unparsed_value: PageElement):
        self.rooms_count = int(unparsed_value.findNext("span", {"class": "main-param"}).text.split("-")[0])

    def set_price(self, unparsed_price: PageElement):
        number_strings = unparsed_price.findNext("span", {"class": "main-param"}).text.replace(u'\xa0', u' ').split(
            " ")
        number_strings.pop()
        self.price = int(''.join(number_strings))

    def set_address(self, unparsed_address: PageElement):
        self.address = unparsed_address.text[5:]

    def set_area(self, unparsed_area: PageElement):
        self.area = float(unparsed_area.text.replace(u'\xa0', u' ').split(" ")[1])

    def set_description(self, unparsed_description: PageElement):
        self.description = unparsed_description.text
