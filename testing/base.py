import django.contrib.auth.models
import django.contrib.contenttypes.models
import django.urls
import rest_framework.test


class UserAwareTestCase(rest_framework.test.APITestCase):
    DEFAULT_PASSWORD = "1Th!password"

    def setUp(self):
        from users.tests.factories import user_factory

        self.user = user_factory.create(is_staff=False, password=self.DEFAULT_PASSWORD)
        self.get_token(self.user)

    def get_token(self, user, authenticate=True):
        response = self.client.post(
            django.urls.reverse("tokens"),
            {"username": user.username, "password": self.DEFAULT_PASSWORD},
        )

        token = response.json()["access"]
        if authenticate:
            self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        return token
