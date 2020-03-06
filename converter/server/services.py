import urllib.request
import xml.etree.ElementTree as ET
from collections import UserDict
from datetime import datetime
from time import time


class UrlError(Exception):
    pass


class Currency(UserDict):

    def __init__(self, url, update_interval=15):
        super().__init__()
        self.url = url
        self._update_interval = update_interval
        self._last_update = 0
        self.load_currency_from_server()

    def load_currency_from_server(self):
        request = urllib.request.urlopen(self.url)
        if request.status != 200:
            raise UrlError(f"Can't access: {self.url}")
        data = request.read()
        tree = ET.fromstring(data)
        for node in tree.iter():
            print(node)

    def __getitem__(self, item):
        if (time() - self._last_update) > self._update_interval * 60:
            self.load_currency_from_server()
        return self.data[item]


c = Currency(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={datetime.now().strftime("%d/%m/%Y")}')


