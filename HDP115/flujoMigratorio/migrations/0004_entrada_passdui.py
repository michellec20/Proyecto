# Generated by Django 4.0.4 on 2022-06-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flujoMigratorio', '0003_alter_persona_dui_alter_persona_pasaporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='passDui',
            field=models.CharField(default='', max_length=10),
        ),
    ]
