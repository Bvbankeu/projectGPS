from django.shortcuts import render

# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse
from urllib.parse import urlparse, parse_qs
from position.models import GpsCoordinates, GpsModule
import datetime

def date_conversion(date):
    annee_hex = hex(date.year-2000)[2:].zfill(2)
    mois_hex = hex(date.month)[2:].zfill(2)
    jour_hex = hex(date.day)[2:].zfill(2)
    heure_hex = hex(date.hour)[2:].zfill(2)
    minutes_hex = hex(date.minute)[2:].zfill(2)
    secondes_hex = hex(date.second)[2:].zfill(2)
    date_hex = annee_hex + mois_hex + jour_hex + heure_hex + minutes_hex + secondes_hex
    # Concaténer les composants en une seule chaîne hexadécimale
    return date_hex 

@csrf_exempt
# Vue pour décoder le message hexadécimal
def login(request):
    if request.method == 'GET':
        hex_message = request.GET.get('hex_message', '')
        #payload = request.body
        #hex_message = payload.get('hex_message')  # Récupérer le message hexadécimal du corps de la requête POST
        #decoded_message = bytes.fromhex(hex_message).decode('utf-8')  # Décoder le message hexadécimal
        if hex_message[2:4] == '01':
            imei = hex_message[4:16]
            return JsonResponse({'response': '787801010D0A'})
        else:
            return JsonResponse({'response': '787801440D0A'})
    else:
        return JsonResponse({'error': 'Methode non autorisee'}, status=405)


def onlineGPS(request):
    if request.method == 'GET':
        hex_message = request.GET.get('hex_message', '')
        imei_message = request.GET.get('imei', '')
        # Créer un objet GpsCoordinates en lui affectant les valeurs nécessaires
        gps_module, created = GpsModule.objects.get_or_create(id=imei_message, defaults={
            'id': imei_message,
            'battery': 0.0,  # Ajoutez d'autres valeurs par défaut si nécessaire
            'simNumber': '', 
            'idEnfant': 0,
        })
        gps_coordinates = GpsCoordinates.objects.create(
            date=GpsCoordinates.date_conversion(hex_message[4:16]),
            latitude=GpsCoordinates.coordinates_conversion(hex_message[18:26]),
            longitude=GpsCoordinates.coordinates_conversion(hex_message[26:34]),
            gpsModule=gps_module
        )
        #gps_coordinates.date = gps_coordinates.date_conversion(hex_message[:12])
        data_gps_info_length = hex_message[16:17]
        data_gps_satelitte_num = hex_message[17:18]
        #gps_coordinates.latitude = gps_coordinates.coordinates_conversion(hex_message[14:22])
        #gps_coordinates.longitude = gps_coordinates.coordinates_conversion(hex_message[22:30])
        data_gps_speed = hex_message[34:36]
        data_gps_status_heading = hex_message[36:40]
        #gps_coordinates.gpsModule = 654687

        insert_url = 'http://localhost:8000/api/gpsCoordinates/'

        gps_coordinates.save
        date_now = datetime.datetime.now()
        response = '78780010'+hex_message[4:16]+'0D0A'

        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Methode non autorisee'}, status=405)

def offlineGPS(request):
    if request.method == 'GET':
        hex_message = request.GET.get('hex_message', '')
        imei_message = request.GET.get('imei', '')
        # Créer un objet GpsCoordinates en lui affectant les valeurs nécessaires
        gps_module, created = GpsModule.objects.get_or_create(id=imei_message, defaults={
            'id': imei_message,
            'battery': 0.0,  # Ajoutez d'autres valeurs par défaut si nécessaire
            'simNumber': '', 
            'idEnfant': 0,
        })
        gps_coordinates = GpsCoordinates.objects.create(
            date=GpsCoordinates.date_conversion(hex_message[4:16]),
            latitude=GpsCoordinates.coordinates_conversion(hex_message[18:26]),
            longitude=GpsCoordinates.coordinates_conversion(hex_message[26:34]),
            gpsModule=gps_module
        )
        #gps_coordinates.date = gps_coordinates.date_conversion(hex_message[:12])
        data_gps_info_length = hex_message[16:17]
        data_gps_satelitte_num = hex_message[17:18]
        #gps_coordinates.latitude = gps_coordinates.coordinates_conversion(hex_message[14:22])
        #gps_coordinates.longitude = gps_coordinates.coordinates_conversion(hex_message[22:30])
        data_gps_speed = hex_message[34:36]
        data_gps_status_heading = hex_message[36:40]
        #gps_coordinates.gpsModule = 654687

        insert_url = 'http://localhost:8000/api/gpsCoordinates/'

        gps_coordinates.save
        date_now = datetime.datetime.now()
        response = '78780011'+hex_message[4:16]+'0D0A'

        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Methode non autorisee'}, status=405)



def reste(request):
    if request.method == 'GET':
        return JsonResponse({'response': '787801010D0A'})
    
def status(request):
    if request.method == 'GET':
        response = request.GET.get('hex_message', '')
        response = '7878'+response+'0D0A'
        return JsonResponse({'response': response})
    
def offlineWifi(request):
    if request.method == 'GET':
        response = request.GET.get('hex_message', '')
        date_now = datetime.datetime.now()
        response = '78780017'+response[4:16]+'0D0A'
        return JsonResponse({'response': response})


def wifiPositioning(request):
    if request.method == 'GET':
        response = request.GET.get('hex_message', '')
        date_now = datetime.datetime.now()
        response = '78780069'+response[4:16]+'0D0A'
        return JsonResponse({'response': response})