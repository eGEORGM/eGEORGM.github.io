# Generated by Django 4.1.7 on 2023-03-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_alter_employe_homeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='住址'),
        ),
    ]
