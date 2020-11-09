# Generated by Django 3.1.1 on 2020-10-13 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=3, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(max_length=18)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=40)),
                ('apellido_materno', models.CharField(max_length=40)),
                ('sexo', models.CharField(max_length=6)),
                ('estado_civil', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('rfc', models.CharField(max_length=13)),
                ('nss', models.CharField(max_length=11)),
                ('correo_electronico', models.CharField(max_length=100)),
                ('telefono_casa', models.CharField(max_length=20)),
                ('telefono_celular', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('folder_at', models.CharField(blank=True, max_length=50)),
                ('status_at', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'Origen'), (2, 'Actual'), (3, 'Egresado')], default=1)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('pais', models.CharField(max_length=50)),
                ('entidad', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=80)),
                ('ciudad', models.CharField(max_length=80)),
                ('calle', models.CharField(max_length=200)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('graduado', models.BooleanField(default=False)),
                ('graduado_fecha', models.DateField()),
                ('old_matricula', models.CharField(max_length=10)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='v1.persona')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.alumnocategoria')),
            ],
        ),
    ]