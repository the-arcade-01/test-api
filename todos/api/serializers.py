from rest_framework import serializers
from .models import Todo

# custom data can also be serialized
# but here we serialized Todo model

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        