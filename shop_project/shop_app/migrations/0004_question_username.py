# Generated by Django 2.1.3 on 2018-12-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='username',
            field=models.CharField(default='', max_length=264),
        ),
    ]