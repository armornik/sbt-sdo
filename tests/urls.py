from django.urls import path

from .views import test_a, test_b, exit_test_a, exit_test_b

app_name = 'tests'

urlpatterns = [
    path('test-a', test_a, name='test_a'),
    path('test-b', test_b, name='test_b'),
    path('exit-test-a', exit_test_a, name='exit_test_a'),
    path('exit-test-b', exit_test_b, name='exit_test_b'),
]
