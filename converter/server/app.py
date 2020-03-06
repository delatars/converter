from .router_dispatcher import RoutersDispatcher
from .handlers.handlers_processor import HandlersProcessor
from .handlers import root


def setup_app():
    handlers_processor = HandlersProcessor(RoutersDispatcher())

    handlers_processor.routers.add_get("/", root)
    return handlers_processor

