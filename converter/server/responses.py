import json
from http.server import BaseHTTPRequestHandler
from typing import Callable, Optional, Any, Tuple, List

from .errors import ERROR_DESCRIPTIONS, ERROR_HTTP_STATUSES

JsonEncoder = Callable[[Any], str]
JsonSerializable = Any


class JsonResponse:

    def __init__(self,
                 data: JsonSerializable,
                 status: int = 200,
                 reason: Optional[str] = None,
                 dumps: JsonEncoder = json.dumps,
                 headers: List[Tuple[str, str]] = None,
                 charset: str = "utf8"
                 ):
        self.status = status
        if not reason:
            self.reason = BaseHTTPRequestHandler.responses[status]
        self.content_type = 'application/json'
        self.body = dumps(data).encode(charset)
        # we can do header processing to ensure of correct structure
        if not headers:
            self.headers = []

        self.headers.append(('Content-Type', 'application/json'))


def error(code, error_data=None, error_message=None):
    resp = {
        'errorCode': code,
        'errorMessage': error_message or ERROR_DESCRIPTIONS.get(code),
        'success': False
    }
    if error_data is not None:
        resp['errorData'] = error_data
    return JsonResponse(resp, status=ERROR_HTTP_STATUSES.get(code) or 400)


def success(data=None):
    return JsonResponse({
        'data': data,
        'success': True
    })
