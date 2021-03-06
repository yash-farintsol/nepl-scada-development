# Generated by Django 3.2.9 on 2022-02-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nivdas', '0007_auto_20220215_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_group',
            name='admin_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='admin_group',
            name='audit_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='admin_group',
            name='help_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='admin_group',
            name='history_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='admin_group',
            name='master_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='admin_group',
            name='supervise_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='operator_group',
            name='admin_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='operator_group',
            name='audit_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='operator_group',
            name='help_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='operator_group',
            name='history_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='operator_group',
            name='master_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='operator_group',
            name='supervise_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supervise_group',
            name='admin_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supervise_group',
            name='audit_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supervise_group',
            name='help_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supervise_group',
            name='history_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supervise_group',
            name='master_page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supervise_group',
            name='supervise_page',
            field=models.CharField(max_length=500),
        ),
    ]
