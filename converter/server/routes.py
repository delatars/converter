from converter.server.handlers.converter import currencies, convert


def setup_routes(app):
    app.routers.add_get("/currencies", currencies)
    app.routers.add_get("/currencies/convert", convert)
