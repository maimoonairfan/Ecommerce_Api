from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListAuthorityAPIView.as_view(),name="AuthorityList"),
    path("create/", views.CreateAuthorityAPIView.as_view(),name="Authority_create"),
    path("update/<int:pk>/",views.UpdateAuthorityAPIView.as_view(),name="update_Authority"),
    path("delete/<int:pk>/",views.DeleteAuthorityAPIView.as_view(),name="delete_Authority")
]