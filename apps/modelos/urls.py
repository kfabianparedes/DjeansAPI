from rest_framework.routers import DefaultRouter

from .views.modelo_view import ModeloView

router = DefaultRouter()
router.register(r'', ModeloView, basename='modelos')

urlpatterns = router.urls
