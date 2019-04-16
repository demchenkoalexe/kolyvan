from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('list_products', views.showListProducts),
    path('admins', views.admin)
]

