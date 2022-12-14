# Generated by Django 4.0.5 on 2022-07-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderid', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.IntegerField()),
                ('uid', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('pprice', models.CharField(max_length=10)),
                ('amount', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='info',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
