from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("core.urls")),
    path('users/',include("users.urls")),
    path('oauth/', include('social_django.urls', namespace='social')),
]
