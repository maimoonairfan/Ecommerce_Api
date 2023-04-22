from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListCartAPIView.as_view(),name="CartList"),
    path("create/", views.CreateCartAPIView.as_view(),name="Cart_create"),
    path("update/<int:pk>/",views.UpdateCartAPIView.as_view(),name="update_Cart"),
    path("delete/<int:pk>/",views.DeleteCartAPIView.as_view(),name="delete_Cart")
]