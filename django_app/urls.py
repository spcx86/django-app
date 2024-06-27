from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from myapp.views import HelloWorldView, callback
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/', include('myapp.urls')),
    path('callback/', callback, name='callback'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
