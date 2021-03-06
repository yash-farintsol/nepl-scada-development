# Generated by Django 3.2.9 on 2022-02-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=30)),
                ('pswd', models.CharField(max_length=30)),
                ('pswchdu', models.IntegerField()),
                ('group_name', models.CharField(max_length=20)),
                ('dept_name', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('sadmin', models.BooleanField()),
                ('ucdate', models.DateTimeField(auto_now_add=True)),
                ('pscdate', models.DateTimeField()),
                ('psedate', models.DateTimeField()),
                ('adpages', models.CharField(max_length=50)),
            ],
        ),
    ]
