# Generated by Django 3.1.8 on 2022-06-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='Ikwuje Peace', max_length=200),
        ),
    ]
