"""sdo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('info.urls', namespace='info'), name='index'),
    path('info/', include('info.urls', namespace='info'), name='index'),
    path('tests/', include('tests.urls', namespace='tests'), name='test'),
    path('studyapp/', include('studyapp.urls', namespace='studyapp'), name='study'),
    # path('auth/', include('authapp.urls', namespace='authapp'), name='auth'),
    path('', include('authapp.urls', namespace='authapp'), name='auth'),
]