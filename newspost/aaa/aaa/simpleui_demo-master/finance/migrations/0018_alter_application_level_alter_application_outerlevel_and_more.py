# Generated by Django 4.1.7 on 2023-07-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0017_application_applytime_alter_application_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='level',
            field=models.IntegerField(choices=[(1, '中'), (0, '低'), (2, '高')], default=0, verbose_name='严重程度'),
        ),
        migrations.AlterField(
            model_name='application',
            name='outerlevel',
            field=models.IntegerField(choices=[(0, '1'), (3, '4'), (4, '5'), (2, '3'), (1, '2')], default=0, verbose_name='外部等级'),
        ),
        migrations.AlterField(
            model_name='defaultperson',
            name='level',
            field=models.IntegerField(choices=[(1, '中'), (0, '低'), (2, '高')], default=0, verbose_name='严重程度'),
        ),
        migrations.AlterField(
            model_name='defaultperson',
            name='outerlevel',
            field=models.IntegerField(choices=[(0, '1'), (3, '4'), (4, '5'), (2, '3'), (1, '2')], default=0, verbose_name='外部等级'),
        ),
    ]
