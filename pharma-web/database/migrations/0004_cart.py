# Generated by Django 5.1.3 on 2024-11-29 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_clientes_senha'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.medicamentos')),
            ],
        ),
    ]