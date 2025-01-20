from django.urls import path
from modules.users.views import UserView, UserDetailView

urlpatterns = [
    path("users/", UserView.as_view(), name="users"),
    path("users/<int:user_id>/", UserDetailView.as_view(), name="user-detail"),
]
