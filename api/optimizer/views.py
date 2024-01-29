from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def optimizer_api(request):
    """
    This is the API for the optimizer.

    NOTE: not implemented yet.
    """
    return Response("Welcome to the Markowitz optimizer API.")
