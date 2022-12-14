'''Required imports'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainblog.urls')),
    path('signup/', include('django.contrib.auth.urls')),
    path('signup/', include('signup.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
