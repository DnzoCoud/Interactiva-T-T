from django.urls import path
from modules.users.views import UserCreateView, UserListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/", UserCreateView.as_view(), name="user_save"),
]
