# Generated by Django 2.1.3 on 2018-11-12 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Cargo')),
                ('abreviacao', models.CharField(max_length=10, verbose_name='Abreviação')),
            ],
        ),
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('status', models.CharField(choices=[('Aberto', 'Aberto'), ('Arquivado', 'Arquivado'), ('Cancelado', 'Cancelado')], default='Aberto', max_length=10, verbose_name='Status')),
                ('assunto', models.CharField(max_length=30, verbose_name='Assunto')),
                ('referencia', models.CharField(max_length=30, verbose_name='Referência')),
                ('anexo', models.CharField(max_length=30, verbose_name='Anexo')),
                ('data', models.DateField(verbose_name='Data')),
                ('data_missao', models.DateField(verbose_name='Data da Missão')),
                ('destino', models.CharField(max_length=30, verbose_name='Destino')),
                ('conteudo', tinymce.models.HTMLField(verbose_name='Conteúdo')),
                ('arquivo', models.FileField(default='sadasd.pdf', upload_to='oficios_arquivo')),
            ],
            options={
                'verbose_name_plural': 'Ofícios',
                'db_table': 'p1_oficios',
            },
        ),
        migrations.CreateModel(
            name='Opm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='OPM')),
            ],
        ),
        migrations.CreateModel(
            name='PolicialMilitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem_up', models.ImageField(blank=True, null=True, upload_to='pm_imagens/', verbose_name='Modificar Imagem')),
                ('matricula', models.CharField(default='00000000', max_length=8, unique=True, verbose_name='Matrícula')),
                ('numero', models.CharField(default=0, max_length=6, verbose_name='Número')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('nome_guerra', models.CharField(max_length=30, verbose_name='Nome de Guerra')),
                ('data_nascimento', models.DateField(verbose_name='Data Nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('tipo_sanguineo', models.CharField(choices=[('A-', 'A-'), ('A+', 'A+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('B-', 'B-'), ('B+', 'B+'), ('O-', 'O-'), ('O+', 'O+')], max_length=3, verbose_name='Tipo Sanguíneo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('rg', models.CharField(max_length=15, verbose_name='RG')),
                ('telefone1', models.CharField(max_length=10, verbose_name='Telefone 1')),
                ('telefone2', models.CharField(max_length=10, verbose_name='Telefone 2')),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p1.Cargo', verbose_name='Cargo')),
                ('opm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p1.Opm', verbose_name='OPM')),
            ],
            options={
                'verbose_name': 'Policial Militar',
                'verbose_name_plural': 'Policiais',
                'db_table': 'p1_policiais',
            },
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('boletim', models.CharField(max_length=30)),
                ('descricao', models.TextField(max_length=300)),
                ('publicacoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.PolicialMilitar')),
            ],
            options={
                'verbose_name': 'Publicação',
                'verbose_name_plural': 'Publicações',
                'db_table': 'p1_publicacoes',
            },
        ),
        migrations.CreateModel(
            name='SituacaoFuncional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Situação Funcional',
                'verbose_name_plural': 'Situação Funcional',
                'db_table': 'p1_situacaofuncional',
            },
        ),
        migrations.CreateModel(
            name='TipoOficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=60)),
                ('assunto', models.CharField(max_length=30, verbose_name='Assunto')),
                ('referencia', models.CharField(max_length=30, verbose_name='Referência')),
                ('anexo', models.CharField(max_length=30, verbose_name='Anexo')),
                ('destino', models.CharField(max_length=30, verbose_name='Destino')),
                ('conteudo', tinymce.models.HTMLField(verbose_name='Conteúdo')),
            ],
            options={
                'verbose_name': 'Tipo de Ofício',
                'verbose_name_plural': 'Tipos de Ofício',
                'db_table': 'p1_tipos_oficio',
            },
        ),
        migrations.CreateModel(
            name='TipoPublicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo de Publicação',
                'verbose_name_plural': 'Tipos de Publicação',
                'db_table': 'p1_tipos_publicacao',
            },
        ),
        migrations.AddField(
            model_name='publicacao',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='p1.TipoPublicacao'),
        ),
        migrations.AddField(
            model_name='policialmilitar',
            name='situacao_funcional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p1.SituacaoFuncional', verbose_name='Situação Funcional'),
        ),
        migrations.AddField(
            model_name='oficio',
            name='tipo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='p1.TipoOficio', verbose_name='Tipo'),
        ),
    ]
