# Generated by Django 3.2.9 on 2022-03-29 10:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nivdas', '0013_auto_20220328_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime(2022, 3, 29, 16, 9, 28, 112776))),
                ('Time', models.TimeField(default=datetime.time(16, 9, 28, 112776))),
                ('Comment', models.TextField()),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nivdas.user')),
            ],
        ),
    ]
