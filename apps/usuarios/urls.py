from rest_framework.routers import DefaultRouter

from apps.usuarios.views.usuario.cambiar_password_view import PasswordView
from apps.usuarios.views.usuario.usuario_view import UsuarioView

router = DefaultRouter()
router.register(r'', UsuarioView, basename='usuarios')
router.register(r'password', PasswordView, basename='password')
urlpatterns = router.urls
