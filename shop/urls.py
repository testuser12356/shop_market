from django.urls import path

import shop.views as views

urlpatterns = [
    path("", views.home, name="home"),
    path("product-filter/", views.product_filter, name="product_filter"),
    path("add-to-favorite/", views.add_to_favorite, name="add_to_favorite"),
    path("product-list/<int:category_id>", views.product_list, name="product_list"),
]
