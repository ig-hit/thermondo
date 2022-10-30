from django.urls import re_path
from rest_framework.routers import SimpleRouter

from users import views

router = SimpleRouter()
router.register("users", views.RegistrationView, "users")

urlpatterns = router.urls + [
    re_path(r"tokens/?", views.TokenView.as_view(), name="tokens"),
]
