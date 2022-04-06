from rest_framework.routers import DefaultRouter
from .views.sucursal_view import SucursalView

router = DefaultRouter()
router.register(r'', SucursalView, basename='sucursales')

urlpatterns = router.urls
