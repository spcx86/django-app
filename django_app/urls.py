from django.contrib import admin
from django.urls import path, include
from myapp.views import HelloWorldView, callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('myapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('callback/', callback, name='callback'),  # Add this line
]