# Generated by Django 3.2.9 on 2022-02-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nivdas', '0008_auto_20220215_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_member',
            name='adpages',
            field=models.CharField(max_length=500),
        ),
    ]
