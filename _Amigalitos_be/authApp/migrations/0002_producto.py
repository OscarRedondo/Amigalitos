# Generated by Django 3.2.7 on 2021-10-04 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('producto_nombre', models.CharField(default='-', max_length=40)),
                ('producto_precio', models.IntegerField(default=0)),
                ('producto_descripcion', models.DateTimeField()),
                ('producto_miniatura', models.CharField(default='-', max_length=40)),
                ('producto_categoria', models.CharField(default='-', max_length=40)),
                ('producto_vencimiento', models.DateTimeField()),
                ('producto_stock', models.IntegerField(default=0)),
                ('producto_imagenes', models.CharField(default='-', max_length=40)),
            ],
        ),
    ]