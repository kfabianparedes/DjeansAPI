from rest_framework.routers import DefaultRouter
from .views.detalle_de_compra_view import DetalleDeCompraView

router = DefaultRouter()
router.register(r'', DetalleDeCompraView, basename='detalles_de_compra')

urlpatterns = router.urls
