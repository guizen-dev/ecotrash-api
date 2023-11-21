from rest_framework import serializers
from .models import Recycle

class RecycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle
        fields = '__all__'