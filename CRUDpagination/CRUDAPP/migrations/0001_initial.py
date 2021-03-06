# Generated by Django 4.0.5 on 2022-06-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_pan', models.CharField(max_length=50)),
                ('customer_adhar', models.IntegerField()),
            ],
        ),
    ]
