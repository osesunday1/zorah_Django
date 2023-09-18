from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('all-product', views.all_products, name='all-products'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('packages/<slug:packages_slug>/', views.store, name='products_by_packages'),
    path('surprises/<slug:surprises_slug>/', views.store, name='products_by_surprises'),
   # path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path ('productdetail/<int:pk>/', views.productdetail, name="productdetail"),
]
