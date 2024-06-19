from django.urls import path
from .views import HelloWorldView, callback


urlpatterns = [
    path('hello_world/', HelloWorldView.as_view(), name='hello_world'),
    path('callback/', callback, name='callback'),

]