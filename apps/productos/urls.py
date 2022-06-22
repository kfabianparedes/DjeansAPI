from rest_framework.routers import DefaultRouter

from .views.product_list_view import ProductByProviderView
from .views.producto_view import ProductoView

router = DefaultRouter()
router.register(r'', ProductoView, basename='productos')
router.register(r'proveedor', ProductByProviderView, basename='list-by-provider')

urlpatterns = router.urls
