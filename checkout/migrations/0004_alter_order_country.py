# Generated by Django 3.2.7 on 2021-10-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
