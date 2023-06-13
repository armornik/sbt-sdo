from django.urls import path

from .views import index, study, studying

app_name = 'info'

urlpatterns = [
    path('study/', study, name='study'),
    path('studying/', studying, name='studying'),
    path('', index, name='index'),
    # path('', index, name='index'),
]
