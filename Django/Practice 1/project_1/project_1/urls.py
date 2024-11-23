
from django.contrib import admin
from django.urls import path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home),
    path('about/', view.about ),
    path('app_1/', include('app_1.urls'))
]
