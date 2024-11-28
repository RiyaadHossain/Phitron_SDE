from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('cars/', include('cars.urls')),
    path('comments/', include('comments.urls')),
    path('profiles/', include('profiles.urls')),
    # path('order_histories/', include('order_histories.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)