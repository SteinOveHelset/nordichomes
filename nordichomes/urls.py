from django.contrib import admin
from django.urls import path

from core.views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
]
