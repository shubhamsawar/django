from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.SignUp, name = 'signup'),
    path('',views.login_user, name='login'),
    path('logout/', views.logout_user, name = 'logout')
]