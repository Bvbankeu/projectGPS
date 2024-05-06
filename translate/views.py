from django.shortcuts import render

# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse
from urllib.parse import urlparse, parse_qs



@csrf_exempt
# Vue pour décoder le message hexadécimal
def decode_message(request):
    if request.method == 'GET':
        hex_message = request.GET.get('hex_message', '')
        #payload = request.body
        #hex_message = payload.get('hex_message')  # Récupérer le message hexadécimal du corps de la requête POST
        #decoded_message = bytes.fromhex(hex_message).decode('utf-8')  # Décoder le message hexadécimal
        if hex_message[6:8] == '01':
            return JsonResponse({'decoded_message': '787801010D0A'})
        else:
            return JsonResponse({'decoded_message': '787801440D0A'})
    else:
        return JsonResponse({'error': 'Methode non autorisee'}, status=405)
