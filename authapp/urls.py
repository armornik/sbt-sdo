from django.urls import path

from .views import login, logout, RegisterCreateView

app_name = 'authapp'

urlpatterns = [
    # path('login/', login, name='login'),
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterCreateView.as_view(), name='register'),
]
