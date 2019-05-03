from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('list_products', views.showListProducts),
    path('admins', views.admin),
    path('product', views.product),
    path('editAdmin', views.editAdmin),
    path('saveEdit', views.saveEdit),
    path('addProduct', views.addProduct),
    path('saveAdd', views.saveAdd), 
    path('delete', views.delete)
]

