import json
from django.http import JsonResponse

from .models import Subscriber

def api_add_subscriber(request):
    # Receiving data
    data = json.loads(request.body)
    email = data['email']
    # Creating Subscriber
    s = Subscriber.objects.create(email=email)

    return JsonResponse({'success': True})