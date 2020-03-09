from converter.server.responses import error, JsonResponse
from converter.server.errors import ERROR_NOT_FOUND
from .handlers_processor import HandlersProcessor


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

    def _process_request(self, request: HandlersProcessor) -> JsonResponse:
        try:
            handler = self._routers[request.http_method][request.path]
        except KeyError:
            return error(ERROR_NOT_FOUND)
        # we could make a middlewares processing there
        result = handler(request)
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