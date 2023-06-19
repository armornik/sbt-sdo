from django.urls import path

from .views import test_a, test_b, test_c, test_d, exit_test_a, exit_test_b, exit_test_c, exit_test_d

app_name = 'tests'

urlpatterns = [
    path('test-a', test_a, name='test_a'),
    path('test-b', test_b, name='test_b'),
    path('test-c', test_c, name='test_c'),
    path('test-d', test_d, name='test_d'),
    path('exit-test-a', exit_test_a, name='exit_test_a'),
    path('exit-test-b', exit_test_b, name='exit_test_b'),
    path('exit-test-c', exit_test_c, name='exit_test_c'),
    path('exit-test-d', exit_test_d, name='exit_test_d'),
]
