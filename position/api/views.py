from rest_framework import viewsets
from position.models import *
from .serializers import *

class GpsModuleViewSet(viewsets.ModelViewSet):

    serializer_class = GpsModuleSerializer
    def get_queryset(self):
        # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = GpsModule.objects.all()
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        GpsModule_id = self.request.GET.get('id')
        if GpsModule_id is not None:
            queryset = queryset.filter(id=GpsModule_id)
        return queryset
    
    


class GpsCoordinatesViewSet(viewsets.ModelViewSet):

    queryset = GpsCoordinates.objects.all()
    serializer_class = GpsCoordinatesSerializer