from rest_framework import serializers
from django.contrib.auth import get_user_model
from chat.models import Thread, ChatMessage

User = get_user_model()

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'