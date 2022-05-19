from rest_framework.routers import DefaultRouter
from .views.compra_view import CompraView

router = DefaultRouter()
router.register(r'', CompraView, basename='compras')

urlpatterns = router.urls
