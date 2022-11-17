from django.urls import path,include
from . import views
urlpatterns = [
    path('details/<int:pk>',views.product_details,name='product_detail'),
    path('list/',views.product_list,name='product_list'),
    # path('category/<int:pk>',views.categories,name='categories')
]
