from rest_framework.routers import DefaultRouter
from .views.tienda_view import TiendaView

router = DefaultRouter()
router.register(r'', TiendaView, basename='tiendas')

urlpatterns = router.urls
