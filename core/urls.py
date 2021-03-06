from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.roles.views.rol_view import RolView
from apps.tipo_comprobante.views import TipoComprobanteView
from apps.usuarios.views.autenticacion.login_view import Login
from apps.usuarios.views.autenticacion.logout_view import Logout
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from apps.usuarios.views.estado_civil.estado_civil_view import EstadoCivilView
from apps.usuarios.views.informacion_personal.informacion_personal_view import InformacionPersonalView
from apps.usuarios.views.tipo_de_documento.tipo_de_documento_view import TipoDeDocumentoView

router = DefaultRouter()
router.register('tipos-de-documento', TipoDeDocumentoView, basename='tiposDeDocumento')
router.register('informacion-personal', InformacionPersonalView, basename='informacionPersonal')
router.register('estado-civil', EstadoCivilView, basename='estadoCivil')
router.register('tipos-de-comprobante', TipoComprobanteView, basename='tiposDeComprobante')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('usuarios/', include('apps.usuarios.urls')),
    path('roles/', include('apps.roles.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('proveedores/', include('apps.proveedores.urls')),
    path('sucursales/', include('apps.sucursales.urls')),
    path('tiendas/', include('apps.tiendas.urls')),
    path('colores/', include('apps.colores.urls')),
    path('modelos/', include('apps.modelos.urls')),
    path('tallas/', include('apps.tallas.urls')),
    path('marcas/', include('apps.marcas.urls')),
    path('productos/', include('apps.productos.urls')),
    path('compras/', include('apps.compras.urls')),
    path('nota-de-ingreso/', include('apps.nota_de_ingreso.urls')),
    path('detalles_de_compra/', include('apps.detalles_de_compra.urls')),
    path('reporte_compras/', include('apps.compras.urls')),
    path('inventarios/', include('apps.inventarios.urls')),
    path('reporte-compras/', include('apps.reportes_de_compra.urls')),
    # path('detalles-de-compra/', include('apps.detalles_de_compra.urls')),
    # path('guias-de-remision/', include('apps.guias_de_remision.urls')),

] + router.urls
