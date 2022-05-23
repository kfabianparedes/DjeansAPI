from rest_framework.routers import DefaultRouter

from .views import TipoComprobanteView

router = DefaultRouter()

router.register(r'', TipoComprobanteView, basename='tipoDeComprobante')

urlpatterns = router.urls
