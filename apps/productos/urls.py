from rest_framework.routers import DefaultRouter
from .views.producto_view import ProductoView

router = DefaultRouter()
router.register(r'', ProductoView, basename='productos')

urlpatterns = router.urls
