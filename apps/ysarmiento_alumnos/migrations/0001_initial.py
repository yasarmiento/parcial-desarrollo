# Generated by Django 4.0.4 on 2022-06-01 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ysarmiento_grupos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('idgrupos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ysarmiento_grupos.grupos')),
            ],
        ),
    ]
