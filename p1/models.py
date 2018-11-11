from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField



class PolicialMilitar(models.Model):
    nome = models.CharField(max_length=30)
    nome_guerra = models.CharField(max_length=30)
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(
        verbose_name='Sexo',
        choices=SEXO,
        max_length=1

    )
    TIPO_SANGUINEO = (('A-', 'A-'),
                      ('A+', 'A+'),
                      ('AB-', 'AB-'),
                      ('AB+', 'AB+'),
                      ('B-', 'B-'),
                      ('B+', 'B+'),
                      ('O-', 'O-'),
                      ('O+', 'O+')
    )
    tipo_sanguineo = models.CharField(
        max_length=2,
        choices=TIPO_SANGUINEO,
        verbose_name='Tipo Sanguíneo'
    )
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    rg = models.CharField(verbose_name='RG', max_length=15)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Policiais"
        verbose_name = 'Policial Militar'
        db_table = 'p1_policiais'






class TipoOficio(models.Model):
    tipo = models.CharField(max_length=60)
    assunto = models.CharField(verbose_name='Assunto', max_length=30)
    referencia = models.CharField(verbose_name='Referência', max_length=30)
    anexo = models.CharField(verbose_name='Anexo', max_length=30)
    destino = models.CharField(verbose_name='Destino', max_length=30)
    conteudo = HTMLField(verbose_name='Conteúdo')

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name_plural = "Tipos de Ofício"
        verbose_name = 'Tipo de Ofício'
        db_table = 'p1_tipos_oficio'





class Oficio(models.Model):
    numero = models.CharField(verbose_name='Número', max_length=10, default='0001/ghg')
    STATUS = (
        ('Aberto', 'Aberto'),
        ('Arquivado', 'Arquivado'),
        ('Cancelado', 'Cancelado'),

    )
    status = models.CharField(
        verbose_name='Status',
        max_length=10,
        choices=STATUS,
        default='Aberto',
    )
    tipo = models.ForeignKey(TipoOficio,
                             verbose_name='Tipo',
                             on_delete=models.DO_NOTHING,
                             blank=True,
                             null=True
                             )
    assunto = models.CharField(verbose_name='Assunto', max_length=30)
    referencia = models.CharField(verbose_name='Referência', max_length=30)
    anexo = models.CharField(verbose_name='Anexo', max_length=30)
    data = models.DateField(verbose_name='Data')
    data_missao = models.DateField(verbose_name='Data da Missão')
    destino = models.CharField(verbose_name='Destino', max_length=30)
    conteudo = HTMLField(verbose_name='Conteúdo')
    arquivo = models.FileField(upload_to='oficios_arquivo', max_length=100, default='sadasd.pdf')

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Ofícios"
        db_table = 'p1_oficios'



