from rest_framework import viewsets

from .serializers import HeroSerializer, WeaponSerializer
from .models import Hero, Weapon


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all().order_by('name')
    serializer_class = WeaponSerializer
