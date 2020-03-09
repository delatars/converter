# api errors
ERROR_INVALID_INPUT = 1
ERROR_NOT_IMPLEMENTED = 2
ERROR_NOT_FOUND = 3

# Currency
ERROR_CONVERTATION = 10
ERROR_NO_SUCH_CURRENCY = 11


ERROR_DESCRIPTIONS = {
    ERROR_INVALID_INPUT: 'Invalid input format.',
    ERROR_CONVERTATION: 'Convertation error.',
    ERROR_NO_SUCH_CURRENCY: 'No such currency.',
    ERROR_NOT_IMPLEMENTED: 'Server does not support this operation.',
    ERROR_NOT_FOUND: 'This endpoint does not exist.',
}


ERROR_HTTP_STATUSES = {
    ERROR_INVALID_INPUT: 400,
    ERROR_NOT_FOUND: 404,
    ERROR_NOT_IMPLEMENTED: 501
}
