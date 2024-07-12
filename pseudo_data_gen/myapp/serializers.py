# myapp/serializers.py

from rest_framework import serializers
from .models import MyModel


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ["id", "title", "description", "created_at"]
