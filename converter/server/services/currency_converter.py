import urllib.request
import xml.etree.ElementTree as ET
from collections import UserDict
from time import time


class UrlError(Exception):
    pass


class ConvertationError(Exception):
    pass


class CurrencyError(Exception):
    pass


class CurrencyConverter(UserDict):

    def __init__(self, update_interval=30):
        super().__init__()
        self.url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        self._update_interval = update_interval
        self._last_update = 0
        self.load_currency_from_server()

    def __getitem__(self, item):
        if (time() - self._last_update) > self._update_interval * 60:
            self.load_currency_from_server()
        try:
            value = self.data[item]
        except KeyError as ex:
            raise CurrencyError(ex)
        return value

    def get_currencies(self, *args):
        _currencies = {}
        for arg in args:
            requested_currency = self.get(arg.upper())
            if requested_currency:
                _currencies[arg] = requested_currency
        return _currencies

    def load_currency_from_server(self):
        request = urllib.request.urlopen(self.url)
        if request.status != 200:
            raise UrlError(f"Can't access: {self.url}")
        data = request.read()
        tree = ET.fromstring(data)
        for node in tree.iterfind("Valute"):
            _, charcode, nominal, _, value = list(node)
            self.data[charcode.text] = {"nominal": int(nominal.text),
                                        "value": float(value.text.replace(',', '.'))}

    def convert(self, currency, count, convert_to):
        currency = currency.upper()
        convert_to = convert_to.upper()
        allowed_conversations = {
            **{_currency: ["RUB"] for _currency in self.keys()},
            **{"RUB": self.keys()}
        }
        if convert_to not in allowed_conversations[currency]:
            raise ConvertationError(f"Convert not allowed by server: {currency} -> {convert_to}")

        if currency == "RUB":
            return self._convert_rub_to(convert_to, count)
        else:
            return self._convert_to_rub(currency, count)

    def _convert_to_rub(self, currency, count):
        return count * self[currency]["value"] / self[currency]["nominal"]

    def _convert_rub_to(self, currency, rub_count):
        return rub_count / self[currency]["value"] * self[currency]["nominal"]
