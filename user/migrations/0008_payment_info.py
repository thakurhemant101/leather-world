# Generated by Django 4.0.5 on 2022-07-24 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_payment_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='info',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]
