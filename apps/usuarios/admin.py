from django.contrib import admin
from apps.usuarios.models import Usuario

from apps.usuarios.tipo_de_documento_model import TipoDeDocumento
from apps.usuarios.informacion_personal_model import InformacionPersonal
from apps.usuarios.estado_civil_model import EstadoCivil

admin.site.register(Usuario)
admin.site.register(InformacionPersonal)
admin.site.register(TipoDeDocumento)
admin.site.register(EstadoCivil)
