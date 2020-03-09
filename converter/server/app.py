from converter.server.services import (
    RoutersDispatcher, HandlersProcessor, CurrencyConverter
)
from converter.server.routes import setup_routes


def setup_app():
    handlers_processor = HandlersProcessor(RoutersDispatcher())
    handlers_processor.app["CurrencyConverter"] = CurrencyConverter()
    setup_routes(handlers_processor)

    return handlers_processor
