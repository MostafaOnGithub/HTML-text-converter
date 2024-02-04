from django.contrib import admin
from django.urls import path
from myapp.views import converter_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',converter_view)
]
