from django.urls import path
from . import views


urlpatterns=[
    path('',views.add_product,name='add_product'),
    path('product_lists/',views.product_list,name='product_list'),
    path('edit/<int:id>',views.update_product,name='update_product')
]
