from django.contrib import admin
from django.urls import path, include
from myapp.views import HelloWorldView, callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('allauth.urls')),  # Move this up
    path('', include('django.contrib.auth.urls')),
    path('api/', include('myapp.urls')),
    path('callback/', callback, name='callback'),
]
