from django.urls import path
from modules.users.views import UserView

urlpatterns = [
    path("users/", UserView.as_view(), name="user_rest"),
]
