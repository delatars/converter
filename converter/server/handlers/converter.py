from converter.server.responses import error, success
from converter.server.services import HandlersProcessor
from converter.server.errors import ERROR_INVALID_INPUT, ERROR_CONVERTATION, ERROR_NO_SUCH_CURRENCY
from converter.server.services.currency_converter import ConvertationError, CurrencyError


def currencies(request: HandlersProcessor):
    converter = request.app["CurrencyConverter"]
    requested_currencies = request.query.get("currency")
    if requested_currencies:
        return success(converter.get_currencies(*requested_currencies))

    return success(converter.data)


def convert(request: HandlersProcessor):
    converter = request.app["CurrencyConverter"]
    try:
        req_currency = request.query.get("currency")[0]
        req_count = int(request.query.get("count")[0])
        req_convert_to = request.query.get("convert_to")[0]
    except (ValueError, TypeError):
        return error(ERROR_INVALID_INPUT)

    try:
        convertation_result = converter.convert(req_currency, req_count, req_convert_to)
    except CurrencyError as ex:
        return error(ERROR_NO_SUCH_CURRENCY, str(ex))
    except ConvertationError as ex:
        return error(ERROR_CONVERTATION, str(ex))

    return success(
        {
            "currency": req_currency,
            "count": req_count,
            "convertation_currency": req_convert_to,
            "convertation_result": convertation_result,
        }
    )