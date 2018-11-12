from django.contrib import admin
from django.utils.html import mark_safe
from .models import PolicialMilitar
from .models import Oficio
from .models import TipoOficio
from .models import Opm
from .models import Cargo
from .models import SituacaoFuncional
from .models import Publicacao
from .models import TipoPublicacao



class TipoPublicacaoAdmin(admin.ModelAdmin):
    fields = [('nome')]
    list_display = ['nome']



class CargoAdmin(admin.ModelAdmin):
    fields = [('nome', 'abreviacao')]
    list_display = ('nome', 'abreviacao')

class SituacaoFuncionalAdmin(admin.ModelAdmin):
    fields = [('nome')]
    list_display = ['nome']

class OpmAdmin(admin.ModelAdmin):
    fields = ['nome']
    list_display = ('id', 'nome')


class OficioAdmin(admin.ModelAdmin):
    fields = [('data', 'data_missao', 'status'), ('tipo', 'assunto'), ('referencia', 'anexo'), 'destino', 'conteudo', 'arquivo' ]
    list_filter = ['status', 'tipo']
    list_display = ('numero', 'data_missao', 'tipo', 'assunto','status')
    search_fields = ['numero', 'status', 'tipo__tipo']
    date_hierarchy = 'data'
    list_per_page = 15


class PublicacaoInline(admin.TabularInline):
    model = Publicacao
    #raw_id_fields = ("descricao",)
    extra = 1
    classes = ['collapse']


class PolicialAdmin(admin.ModelAdmin):
    #fields = [('data', 'data_missao', 'status'), ('tipo', 'assunto'), ('referencia', 'anexo'), 'destino', 'conteudo' ]
    fieldsets = [
        (None, {'fields': [ ('imagem', 'imagem_up'),
                           ('situacao_funcional'),
                           ('numero', 'matricula'),
                           ('nome', 'nome_guerra'),
                           ('cargo', 'opm')

                          ]

               }
        ),

        ('Dados Pessoais',  {'fields': [('data_nascimento', 'sexo'),
                                        ('tipo_sanguineo', ),
                                        ('telefone1', 'telefone2')

                                        ],
                             'classes': ['collapse']
                             }
        ),
        ('Documentos', {'fields': ['cpf', 'rg'], 'classes': ['collapse']}),
        (None, {'fields': ['added_by']})
    ]
    list_filter = ['cargo__nome']
    list_display = ('matricula', 'cargo','nome', 'nome_guerra', 'cpf', 'rg')
    search_fields = ['numero', 'nome', 'matricula', 'cargo__abreviacao']
    readonly_fields = ["imagem", 'added_by']
    inlines = [PublicacaoInline]

    def imagem(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.imagem_up.url,
            width=120,
            height=160,
        )
        )







class TipoOficioAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    list_per_page = 15






# Register your models here.
admin.site.register(PolicialMilitar, PolicialAdmin)
admin.site.register(Oficio, OficioAdmin)
admin.site.register(TipoOficio, TipoOficioAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Opm, OpmAdmin)
admin.site.register(SituacaoFuncional, SituacaoFuncionalAdmin)
admin.site.register(TipoPublicacao, TipoPublicacaoAdmin)