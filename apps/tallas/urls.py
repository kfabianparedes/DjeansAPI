from rest_framework.routers import DefaultRouter

from .views import TallaView

router = DefaultRouter()

router.register(r'',TallaView, basename='tallas')

urlpatterns = router.urls
