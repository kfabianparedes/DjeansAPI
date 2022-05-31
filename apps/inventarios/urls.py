from rest_framework.routers import DefaultRouter
from .views.views import InventarioView

router = DefaultRouter()
router.register(r'',InventarioView, basename='inventarios')

urlpatterns = router.urls