from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from .responses import error, JsonResponse
from .errors import ERROR_INVALID_INPUT


class HandlerError(Exception):
    pass


class RoutersDispatcher:

    def __init__(self):
        self._routers = {
            "GET": {},
            "POST": {},
            "DELETE": {},
            "HEAD": {},
            "OPTIONS": {},
            "PATCH": {},
            "PUT": {},
        }

    def process_request(self, request: BaseHTTPRequestHandler) -> JsonResponse:
        method, path, _ = request.requestline.split()
        uri = urlparse(path)
        try:
            handler = self._routers[method][uri.path]
        except KeyError:
            return error(ERROR_INVALID_INPUT, f"No such route: {method} {uri.path}")
        result = handler(self)
        if not isinstance(result, JsonResponse):
            raise HandlerError(f"{handler.__name__}: Wrong return value :"
                               f" Handlers must return {JsonResponse} object")
        return result

    def add_route(self, method, path, handler):
        self._routers[method][path] = handler

    def add_get(self, path, handler): self.add_route("GET", path, handler)

    def add_post(self, path, handler): self.add_route("POST", path, handler)

    def add_delete(self, path, handler): self.add_route("DELETE", path, handler)

    def add_head(self, path, handler): self.add_route("HEAD", path, handler)

    def add_options(self, path, handler): self.add_route("OPTIONS", path, handler)

    def add_patch(self, path, handler): self.add_route("PATCH", path, handler)

    def add_put(self, path, handler): self.add_route("PUT", path, handler)