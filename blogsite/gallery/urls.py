from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.list_products , name="index_page"),
    path('product/<int:pk>/' , views.product_detail , name="product_detail") ,
    path('product/<int:pk>/edit' , views.product_edit , name = 'product_edit') , 
    path('product/<int:pk>/delete/' , views.product_delete , name = 'product_delete') , 
]
