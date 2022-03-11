from rest_framework.routers import DefaultRouter

from .views.categoria_view import CategoriaView

router = DefaultRouter()
router.register(r'', CategoriaView, basename='categorias')

urlpatterns = router.urls
