# Generated by Django 3.1.1 on 2020-10-28 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0011_auto_20201027_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lengua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('nombre', models.TextField()),
                ('alias', models.TextField()),
                ('familia', models.TextField()),
                ('agrupacion', models.TextField()),
                ('originaria', models.BooleanField()),
                ('extranjera', models.BooleanField()),
                ('materia', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonaLengua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('read', models.PositiveSmallIntegerField(default=0)),
                ('listening', models.PositiveSmallIntegerField(default=0)),
                ('written', models.PositiveSmallIntegerField(default=0)),
                ('speeking', models.PositiveSmallIntegerField(default=0)),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'Origen'), (2, 'Cursada')])),
                ('comentarios', models.CharField(max_length=200)),
                ('lengua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.lengua')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.persona')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='lenguas',
            field=models.ManyToManyField(through='v1.PersonaLengua', to='v1.Lengua'),
        ),
    ]
