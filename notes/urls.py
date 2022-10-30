from rest_framework.routers import SimpleRouter

from notes import views

router = SimpleRouter()
router.register("", views.NotesView, "notes")

urlpatterns = router.urls
