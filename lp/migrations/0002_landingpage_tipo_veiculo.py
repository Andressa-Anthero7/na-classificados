# Generated by Django 4.1.10 on 2023-08-27 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='tipo_veiculo',
            field=models.CharField(default='Tipo Veículo', max_length=100),
        ),
    ]