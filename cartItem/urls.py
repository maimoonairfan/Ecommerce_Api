from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListCartItemAPIView.as_view(),name="CartItemList"),
    path("create/", views.CreateCartItemAPIView.as_view(),name="CartItem_create"),
    path("update/<int:pk>/",views.UpdateCartItemAPIView.as_view(),name="update_CartItem"),
    path("delete/<int:pk>/",views.DeleteCartItemAPIView.as_view(),name="delete_CartItem")
]