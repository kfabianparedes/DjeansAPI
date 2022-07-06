from rest_framework.routers import DefaultRouter
from .views.nota_ingreso_view import NotaDeIngresoView

router = DefaultRouter()
router.register(r'', NotaDeIngresoView, basename='nota_de_ingreso')

urlpatterns = router.urls
