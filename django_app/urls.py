from django.contrib import admin
from django.urls import path, include
from myapp.views import HelloWorldView, callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('myapp.urls')),
    path('callback/', callback, name='callback'),  # Add this line
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls'))

]