from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import UsersViewSet
from api.views import Service

router = routers.SimpleRouter()
router.register(r"users", UsersViewSet, basename="users")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("markopolo/", Service.as_view(), name='markopolo'),
    path("", include(router.urls))
]