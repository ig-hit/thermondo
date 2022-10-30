from django import urls

import notes.tests.factories
import users.tests.factories
from notes import models
from testing import base

notes_factory = notes.tests.factories.notes_factory
user_factory = users.tests.factories.user_factory


class TestNotesView(base.UserAwareTestCase):
    def test_list(self):
        user = self.user
        n1 = notes_factory.create(user_id=user.id, title="1", body="b1", tags=["1", "foo"])
        n2 = notes_factory.create(user_id=user.id, title="2", tags=["2", "bar"])

        # add some noise
        other_user = user_factory.create(username="foo")
        _ = notes_factory.create(user_id=other_user.id)

        expected = self._make_list_response(n2, n1)

        response = self.client.get(urls.reverse("notes-list"))
        res = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, res)

    def test_list_with_filter_by_tags(self):
        user = self.user
        n1 = notes_factory.create(user_id=user.id, title="1", body="b1", tags=["foo"])
        n2 = notes_factory.create(user_id=user.id, title="2", body="b1", tags=["bar"])
        _ = notes_factory.create(user_id=user.id, title="3", tags=["car"])

        expected = self._make_list_response(n2, n1)

        response = self.client.get(urls.reverse("notes-list") + "?tag=foo&tag=bar")
        res = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, res)

    def test_list_with_filter_by_keyword(self):
        user = self.user
        n1 = notes_factory.create(user_id=user.id, title="1", body="foo text foo")
        n2 = notes_factory.create(user_id=user.id, title="2", body="text")
        _ = notes_factory.create(user_id=user.id, title="other")

        expected = self._make_list_response(n2, n1)

        response = self.client.get(urls.reverse("notes-list") + "?search=text")
        res = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, res)

    def test_list_public(self):
        user = self.user
        _ = notes_factory.create(user_id=user.id, title="1", is_public=False)
        n2 = notes_factory.create(user_id=user.id, title="2", is_public=True)

        expected = self._make_list_response(n2)

        self.client.credentials(HTTP_AUTHORIZATION=None)
        response = self.client.get(urls.reverse("notes-list"))
        res = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, res)

    def test_create(self):
        payload = {
            "title": "the title",
            "body": "notes contents",
            "is_public": True,
            "tags": [
                "foo",
                "bar",
            ],
        }

        response = self.client.post(urls.reverse("notes-list"), data=payload)
        res = response.json()

        self.assertEqual(201, response.status_code)

        entity = models.Note.objects.filter(id=res["id"]).first()
        expected = self._make_details_response(entity)

        self.assertEqual(expected, res)

    def test_update(self):
        user = self.user
        entity = notes_factory.create(user_id=user.id, title="foo", tags=["1", "2"])
        new_title = "bar"
        expected = self._make_details_response(entity)
        expected["title"] = new_title

        response = self.client.patch(
            urls.reverse("notes-detail", kwargs={"pk": entity.id}),
            data={
                "title": new_title,
            },
        )
        res = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, res)

    def test_delete(self):
        user = self.user
        obj = notes_factory.create(user_id=user.id)
        response = self.client.delete(urls.reverse("notes-detail", kwargs={"pk": obj.id}))

        self.assertEqual(204, response.status_code)
        self.assertEqual(0, models.Note.objects.filter(id=obj.id).count())

    def _make_list_response(self, *objs: models.Note):
        return {
            "count": len(objs),
            "next": None,
            "previous": None,
            "results": [self._make_details_response(obj) for obj in objs],
        }

    def _make_details_response(self, obj: models.Note):
        return {
            "id": obj.id,  # type: ignore
            "title": obj.title,
            "body": obj.body,
            "is_public": obj.is_public,
            "tags": [str(t) for t in obj.tags.all()],
        }
