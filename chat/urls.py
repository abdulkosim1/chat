from django.urls import path
from . import views
from chat.views import CreateThreadAPIView, SendMessageAPIView
urlpatterns = [
    path('', views.messages_page),
    path('thread/', CreateThreadAPIView.as_view()),
    path('message/', SendMessageAPIView.as_view()),
]
