from django.db import connections
from django.db.utils import OperationalError
from django.http import HttpResponse, JsonResponse


# Create your views here.
def liveliness(request):
    return HttpResponse("OK")

def readiness(request):
    try:
        connections['default'].cursor()
    except OperationalError:
        return JsonResponse({"ready": False}, status=503)
    else:
        return JsonResponse({"ready": True})
