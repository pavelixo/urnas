from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# project views
from candidates.views import CandidateViewSet
from .views import RootView

router = DefaultRouter()
router.register(r"candidates", CandidateViewSet, basename="candidate")

urlpatterns = [
    path("", RootView.as_view(), name="root-view"),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )