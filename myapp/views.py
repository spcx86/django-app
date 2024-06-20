from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def whats_up(request):
    user = request.user
    if user.is_authenticated:
        first_name = user.first_name
        last_name = user.last_name
        message = f"Hello {first_name} {last_name}! What's up"
    else:
        message = "Hello! What's up unauthenticated user"
    return Response({"message": message})

class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello,,,, worldview gpt what up man!"})

from django.shortcuts import redirect
from django.http import JsonResponse
import requests

def callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)

    token_url = 'http://localhost:8000/o/token/'
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    redirect_uri = 'http://localhost:8000/callback'

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return JsonResponse(response.json())
    return JsonResponse(response.json(), status=response.status_code)



