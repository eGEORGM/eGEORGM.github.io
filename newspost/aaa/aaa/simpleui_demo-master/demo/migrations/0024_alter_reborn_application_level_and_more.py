# Generated by Django 4.1.7 on 2023-07-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0023_alter_reborn_application_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reborn_application',
            name='level',
            field=models.IntegerField(choices=[(1, '中'), (0, '低'), (2, '高')], default=0, verbose_name='严重程度'),
        ),
        migrations.AlterField(
            model_name='reborn_application',
            name='outerlevel',
            field=models.IntegerField(choices=[(1, '2'), (2, '3'), (0, '1'), (3, '4'), (4, '5')], default=0, verbose_name='外部等级'),
        ),
    ]