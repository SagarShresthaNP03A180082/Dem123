
from django.contrib import admin
from django.urls import path
from FaceOfNepal import views

urlpatterns = [
    path('Home/', views.index),
    path('admin/', admin.site.urls),
]
