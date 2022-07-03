from rest_framework import serializers
from pensamentos.models import Pensador

class PensadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pensador
        fields = ['id', 'autor', 'fala']