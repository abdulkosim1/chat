from rest_framework.views import APIView
from account.serializers import RegisterSerializer, ForgotPasswordSerializer,ForgotPasswordCompleteSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import SignUpForm, Loginform
from django.contrib.auth import authenticate, login


User = get_user_model()


class RegisterAPIView(APIView):
    def get(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        return render(request, 'singup.html', {'form': form})
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались. Вам отправлено письмо с активацией', status=201)

def pagelogin(request):

    uservalue=''
    passwordvalue=''

    form= Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("email")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(email=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context= {'form': form,
                      'error': 'The login has been successful'}
            
            return render(request, 'messages.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'login.html', context )

    else:
        context= {'form': form}
        return render(request, 'login.html', context)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Успешно', status=200)
        except User.DoesNotExist:
            return Response('Link expired', status=400)


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_reset_password_code()
        return Response('вам отправлено письмо для восстановления пароля')


class ForgotPasswordCompleteAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно изменен')

