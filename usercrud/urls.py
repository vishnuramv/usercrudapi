from django.urls import path
from .views import ListUserAPIView, CreateUserAPIView, UpdateUserAPIView, DeleteUserAPIView, RetrieveUserAPIView

urlpatterns = [
    path("view/", ListUserAPIView.as_view(),name="user_list"),
    path("view/<int:pk>/", RetrieveUserAPIView.as_view(),name="view_user"),
    path("create/", CreateUserAPIView.as_view(),name="user_create"),
    path("update/<int:pk>/", UpdateUserAPIView.as_view(),name="update_user"),
    path("delete/<int:pk>/", DeleteUserAPIView.as_view(),name="delete_user")
]