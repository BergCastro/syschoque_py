# Generated by Django 2.1.3 on 2018-11-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0002_oficio_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficio',
            name='arquivo',
            field=models.FileField(default='sadasd.pdf', upload_to='oficios_arquivo'),
        ),
    ]
