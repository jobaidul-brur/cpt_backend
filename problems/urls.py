from rest_framework.routers import DefaultRouter

from .views import ProblemViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet, basename='problem')

urlpatterns = router.urls
