from rest_framework.routers import DefaultRouter
from .views.proveedor_view import ProveedorView

router = DefaultRouter()
router.register(r'', ProveedorView, basename='proveedores')

urlpatterns = router.urls