from django.urls import path
from account.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from django.conf.urls import 
from django.conf import settings
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('signup/', signup, name='signup'),
    # path('login/', pagelogin, name='login'), 


    # path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path('reset_password/', ForgotPasswordAPIView.as_view()),
    path('reset_password_complete/', ForgotPasswordCompleteAPIView.as_view())

]