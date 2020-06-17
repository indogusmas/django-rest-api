from .models import Hero, Weapon
from rest_framework import serializers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weapon
        fields = ('name','attack')