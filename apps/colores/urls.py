from rest_framework.routers import DefaultRouter
from .views import ColorView


router = DefaultRouter()
router.register(r'', ColorView, basename='colores')

urlpatterns = router.urls