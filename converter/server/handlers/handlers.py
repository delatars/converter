from converter.server.responses import success


def root(request):
    return success("HelloWorld!")
