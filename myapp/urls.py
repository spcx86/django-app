from django.urls import path
from .views import HelloWorldView, callback, whats_up


urlpatterns = [
    path('hello_world/', HelloWorldView.as_view(), name='hello_world'),
    path('callback/', callback, name='callback'),
    path('whats_up/', whats_up, name='whats_up')
]