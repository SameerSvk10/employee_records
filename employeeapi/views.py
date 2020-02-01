from .resourcegetter import get_employee_records

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# get employees route call
@api_view(["GET"])
def get_employees(request):
    try:
        chunk = request.GET.get('chunk')
        response = get_employee_records(chunk=chunk)
        return Response(response)
    except Exception as e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)
