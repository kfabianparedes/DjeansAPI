from rest_framework.routers import DefaultRouter
from .views.reporte_de_compra import ReporteCompraView

router=DefaultRouter()
router.register(r'',ReporteCompraView,basename='reporte_compras')

urlpatterns=router.urls