from rest_framework.routers import DefaultRouter

from .views import CategoriaView

router = DefaultRouter()
router.register(r'', CategoriaView, basename='usuarios')

urlpatterns = router.urls
