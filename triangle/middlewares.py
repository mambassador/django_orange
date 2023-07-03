from django.http import QueryDict
from django.utils.timezone import now

from triangle.models import Log


class LogMiddleware:
    """Middleware class for logging request information.
    Captures request details and saves them as log entries
    """

    def __init__(self, get_response):
        """Initializes the LogMiddleware instance

        Args:
            get_response(callable): the next middleware or view function
                                    in the chain
        """
        self.get_response = get_response

    def __call__(self, request):
        """Processes the incoming request and logs the request details

        Args:
            request(HttpRequest): the incoming request

        Returns:
            response(HttpResponse): the response generated by the view
                                    function or subsequent middleware.
        """
        response = self.get_response(request)

        if not request.path.startswith("/admin"):
            log = Log(
                path=request.path,
                method=request.method,
                timestamp=now(),
                request_data=self.get_request_data(request),
                status_code=response.status_code,
                user=request.environ.get("USER"),
            )
            log.save()

        return response

    @staticmethod
    def get_request_data(request):
        """Returns the request data based on the request method

        Args:
            request (HttpRequest): The incoming HTTP request object

        Returns:
            request_data(dict): the data stored in GET or POST request
        """
        request_data = {}

        if request.method == "GET":
            request_data = QueryDict(request.META.get("QUERY_STRING")).dict()
        elif request.method == "POST":
            request_data = request.POST.dict()

        return request_data
