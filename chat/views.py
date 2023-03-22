from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

# Create your views here.
from chat.models import Thread, ChatMessage
from django.contrib.auth import get_user_model
from chat.serializers import ThreadSerializer, ChatSerializer

User = get_user_model()

@login_required
# @permission_required
def messages_page(request):
    
    # user = User.objects.all()
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads, 

    }
    return render(request, 'messages.html', context)

class CreateThreadAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = []



class SendMessageAPIView(CreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatSerializer
