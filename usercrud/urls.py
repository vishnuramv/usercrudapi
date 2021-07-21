from django.urls import path
from .views import ListUserAPIView, CreateUserAPIView, UpdateUserAPIView, DeleteUserAPIView

urlpatterns = [
    path("view/", ListUserAPIView.as_view(),name="user_list"),
    path("create/", CreateUserAPIView.as_view(),name="user_create"),
    path("update/<int:pk>/", UpdateUserAPIView.as_view(),name="update_user"),
    path("delete/<int:pk>/", DeleteUserAPIView.as_view(),name="delete_user")
]