# Generated by Django 3.1.1 on 2020-10-14 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_auto_20201013_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.persona'),
        ),
    ]