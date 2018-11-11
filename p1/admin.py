from django.contrib import admin
from django.forms import ModelForm, TextInput
from .models import PolicialMilitar
from .models import Oficio
from .models import TipoOficio

class OficioAdmin(admin.ModelAdmin):
    fields = [('data', 'data_missao', 'status'), ('tipo', 'assunto'), ('referencia', 'anexo'), 'destino', 'conteudo', 'arquivo' ]
    list_filter = ['status', 'tipo']
    list_display = ('numero', 'data_missao', 'tipo', 'assunto','status')
    search_fields = ['numero', 'status', 'tipo__tipo']



class PolicialAdmin(admin.ModelAdmin):
    #fields = [('data', 'data_missao', 'status'), ('tipo', 'assunto'), ('referencia', 'anexo'), 'destino', 'conteudo' ]
    fieldsets = [

    ('Dados Pessoais',  {'fields': [('nome', 'nome_guerra'),
                                        ('data_nascimento', 'sexo')]}),
        ('Documentos', {'fields': ['cpf', 'rg'], 'classes': ['collapse']}),
    ]
   #list_filter = ['status', 'tipo']
   #list_display = ('nome', 'nome_guerra', 'cpf', 'rg')
   #search_fields = ['numero', 'status', 'tipo__tipo']





class TipoOficioAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')





# Register your models here.
admin.site.register(PolicialMilitar)
admin.site.register(Oficio, OficioAdmin)
admin.site.register(TipoOficio, TipoOficioAdmin)