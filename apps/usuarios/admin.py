from django.contrib import admin
from apps.usuarios.clases import EstadoCivil, TipoDocumento
from apps.usuarios.models import InformacionPersonal, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(InformacionPersonal)
admin.site.register(TipoDocumento)
admin.site.register(EstadoCivil)
