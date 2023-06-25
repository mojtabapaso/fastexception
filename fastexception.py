from starlette.exceptions import HTTPException


class FastException:
    class Exceptions:

        def __init__(self, status, message):
            self.status = status
            self.message = message

        def http(self, message=None):
            raise HTTPException(status_code=self.status, detail=message or self.message)

    # --------------2xx----------------
    HTTP_200_OK = Exceptions(status=200, message="OK HTTP")
    HTTP_201_CREATED = Exceptions(status=201, message="Created HTTP")
    HTTP_202_ACCEPTED = Exceptions(status=202, message="Accepted HTTP")
    HTTP_203_NON_AUTHORITATIVE_INFORMATION = Exceptions(status=203, message="Non-Authoritative Information HTTP")
    HTTP_204_NO_CONTENT = Exceptions(status=204, message="No Content HTTP")
    HTTP_205_RESET_CONTENT = Exceptions(status=205, message="Resat content HTTP")
    HTTP_206_PARTIAL_CONTENT = Exceptions(status=206, message="Partial content HTTP")
    HTTP_207_MULTI_STATUS = Exceptions(status=207, message="Multi status HTTP")
    HTTP_208_ALREADY_REPORTED = Exceptions(status=208, message="Already reported HTTP")
    HTTP_226_IM_USED = Exceptions(status=226, message="Im used HTTP")
    # --------------3xx----------------
    HTTP_300_MULTIPLE_CHOICES = Exceptions(status=300, message="Multiple choices HTTP")
    HTTP_301_MOVED_PERMANENTLY = Exceptions(status=301, message="Moved permanently HTTP")
    HTTP_302_FOUND = Exceptions(status=302, message="Found HTTP")
    HTTP_303_SEE_OTHER = Exceptions(status=303, message="See other HTTP")
    HTTP_304_NOT_MODIFIED = Exceptions(status=304, message="Not modified HTTP")
    HTTP_305_USE_PROXY = Exceptions(status=305, message="Use proxy HTTP")
    HTTP_306_RESERVED = Exceptions(status=306, message="Reserved HTTP")
    HTTP_307_TEMPORARY_REDIRECT = Exceptions(status=307, message="Temporary redirect HTTP")
    HTTP_308_PERMANENT_REDIRECT = Exceptions(status=308, message="Permanent HTTP")
    # --------------4xx----------------
    HTTP_400_BAD_REQUEST = Exceptions(status=400, message="Bad Request HTTP")
    HTTP_401_UNAUTHORIZED = Exceptions(status=401, message="Unauthorized HTTP")
    HTTP_402_PAYMENT_REQUIRED = Exceptions(status=402, message="Payment required HTTP")
    HTTP_403_FORBIDDEN = Exceptions(status=403, message="Forbidden HTTP")
    HTTP_404_NOT_FOUND = Exceptions(status=404, message="Not found HTTP")
    HTTP_405_METHOD_NOT_ALLOWED = Exceptions(status=405, message="Method not allowed HTTP")
    HTTP_406_NOT_ACCEPTABLE = Exceptions(status=406, message="Not acceptable HTTP")
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED = Exceptions(status=407, message="Proxy authentication required HTTP")
    HTTP_408_REQUEST_TIMEOUT = Exceptions(status=408, message="Request timeout HTTP")
    HTTP_409_CONFLICT = Exceptions(status=409, message="Conflict HTTP")
    HTTP_410_GONE = Exceptions(status=410, message="Gone HTTP")
    HTTP_411_LENGTH_REQUIRED = Exceptions(status=411, message="Length required HTTP")
    HTTP_412_PRECONDITION_FAILED = Exceptions(status=412, message="Precondition failed HTTP")
    HTTP_413_REQUEST_ENTITY_TOO_LARGE = Exceptions(status=413, message="request entity too large HTTP")
    HTTP_414_REQUEST_URI_TOO_LONG = Exceptions(status=414, message="Request Url too long HTTP")
    HTTP_415_UNSUPPORTED_MEDIA_TYPE = Exceptions(status=415, message="Unsupported media type HTTP")
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = Exceptions(status=416, message="Requested range not satisfiable HTTP")
    HTTP_417_EXPECTATION_FAILED = Exceptions(status=417, message="Expectation failed HTTP")
    HTTP_418_IM_A_TEAPOT = Exceptions(status=418, message="Im a teapot :)")
    HTTP_421_MISDIRECTED_REQUEST = Exceptions(status=421, message="Misdirected request HTTP")
    HTTP_422_UNPROCESSABLE_ENTITY = Exceptions(status=422, message="Unprocessable entity HTTP")
    HTTP_423_LOCKED = Exceptions(status=423, message="Locked HTTP")
    HTTP_424_FAILED_DEPENDENCY = Exceptions(status=424, message="Failed dependency HTTP")
    HTTP_425_TOO_EARLY = Exceptions(status=425, message="Too early HTTP")
    HTTP_426_UPGRADE_REQUIRED = Exceptions(status=426, message="Upgrade Request HTTP")
    HTTP_428_PRECONDITION_REQUIRED = Exceptions(status=428, message="Precondition required HTTP")
    HTTP_429_TOO_MANY_REQUESTS = Exceptions(status=429, message="Too many requests HTTP")
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = Exceptions(status=431, message="request herder fields too large HTTP")
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = Exceptions(status=451, message="Unavailable for legal reasons HTTP")
    # --------------5xx----------------
    HTTP_500_INTERNAL_SERVER_ERROR = Exceptions(status=500, message="Internal server error")
    HTTP_501_NOT_IMPLEMENTED = Exceptions(status=501, message="Not implemented")
    HTTP_502_BAD_GATEWAY = Exceptions(status=502, message="Bad gateway")
    HTTP_503_SERVICE_UNAVAILABLE = Exceptions(status=503, message="Service unavailable")
    HTTP_504_GATEWAY_TIMEOUT = Exceptions(status=504, message="Gateway timeout HTTP")
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED = Exceptions(status=505, message="HTTP version not supported")
    HTTP_506_VARIANT_ALSO_NEGOTIATES = Exceptions(status=506, message="Variant also negotiates HTTP")
    HTTP_507_INSUFFICIENT_STORAGE = Exceptions(status=507, message="Insufficient storage HTTP")
    HTTP_508_LOOP_DETECTED = Exceptions(status=508, message="Loop detected HTTP")
    HTTP_510_NOT_EXTENDED = Exceptions(status=510, message="Not extended HTTP")
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = Exceptions(status=511, message="Network authentication required HTTP")

