from django.urls import path
from modules.authentication.views import AuthTokenView

urlpatterns = [path("auth/login", AuthTokenView.as_view(), name="auth_rest")]
