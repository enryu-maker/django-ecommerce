# Generated by Django 3.2.9 on 2022-05-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_orderplaced_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderplaced',
            options={'verbose_name_plural': 'Order Placed'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Punjab', 'Punjab'), ('Sindh', 'Sindh'), ('Bloachistan', 'Bloachistan'), ('KPK', 'KPK'), ('Gilgit', 'Gilgit')], max_length=50),
        ),
    ]
