from django.contrib import admin
from django.forms import ModelForm, TextInput
from .models import PolicialMilitar
from .models import Oficio
from .models import TipoOficio
from .models import Opm
from .models import Cargo


class CargoAdmin(admin.ModelAdmin):
    fields = [('nome', 'abreviacao')]
    list_display = ('nome', 'abreviacao')

class OpmAdmin(admin.ModelAdmin):
    fields = ['nome']
    list_display = ('id', 'nome')


class OficioAdmin(admin.ModelAdmin):
    fields = [('data', 'data_missao', 'status'), ('tipo', 'assunto'), ('referencia', 'anexo'), 'destino', 'conteudo', 'arquivo' ]
    list_filter = ['status', 'tipo']
    list_display = ('numero', 'data_missao', 'tipo', 'assunto','status')
    search_fields = ['numero', 'status', 'tipo__tipo']



class PolicialAdmin(admin.ModelAdmin):
    #fields = [('data', 'data_missao', 'status'), ('tipo', 'assunto'), ('referencia', 'anexo'), 'destino', 'conteudo' ]
    fieldsets = [
        (None, {'fields': [('numero', 'matricula'),
                           ('nome', 'nome_guerra'),
                           ('cargo', 'opm')

                          ]

               }
        ),

        ('Dados Pessoais',  {'fields': [('data_nascimento', 'sexo'),
                                        ('tipo_sanguineo', ),

                                        ],
                             'classes': ['collapse']
                             }
        ),
        ('Documentos', {'fields': ['cpf', 'rg'], 'classes': ['collapse']}),
    ]
    list_filter = ['cargo__nome']
    list_display = ('matricula', 'cargo','nome', 'nome_guerra', 'cpf', 'rg')
    search_fields = ['numero', 'nome', 'matricula', 'cargo__abreviacao']





class TipoOficioAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')





# Register your models here.
admin.site.register(PolicialMilitar, PolicialAdmin)
admin.site.register(Oficio, OficioAdmin)
admin.site.register(TipoOficio, TipoOficioAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Opm, OpmAdmin)
