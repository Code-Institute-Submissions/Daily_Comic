from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_stock, name='products'),
    path('<int:product_id>/', views.item_detail, name='item_detail'),
    path('addreview/', views.Add_Review, name='add_review'),
    path('addproduct/', views.add_a_product, name='add_a_product'),
    ]
