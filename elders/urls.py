from rest_framework.routers import DefaultRouter
from .views import ElderViewSet


router = DefaultRouter()
router.register(r'elders', ElderViewSet, basename='elders')
urlpatterns = router.urls
