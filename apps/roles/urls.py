from rest_framework.routers import DefaultRouter
from .views.rol_view import RolView

router = DefaultRouter()
router.register(r'', RolView, basename='roles')

urlpatterns = router.urls
