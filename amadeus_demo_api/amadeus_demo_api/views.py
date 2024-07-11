
from amadeus import Client
from django.conf import settings
from django.http import JsonResponse

#amadeus = Client(
  #  client_id=settings.AMADEUS_CLIENT_ID,
  #  client_secret=settings.AMADEUS_CLIENT_SECRET,
   # hostname=settings.AMADEUS_HOSTNAME
#)

def show_amadeus_settings(request):
    return JsonResponse({
        'AMADEUS_CLIENT_ID': settings.AMADEUS_CLIENT_ID,
        'AMADEUS_CLIENT_SECRET': settings.AMADEUS_CLIENT_SECRET,
        'AMADEUS_HOSTNAME': settings.AMADEUS_HOSTNAME
    })