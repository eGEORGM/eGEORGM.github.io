# Generated by Django 4.1.7 on 2023-07-05 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0030_alter_reborn_application_level_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Layer',
        ),
        migrations.AddField(
            model_name='employe',
            name='reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.department', verbose_name='违约原因'),
        ),
        migrations.AddField(
            model_name='reborn_application',
            name='rebornreason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.title', verbose_name='重生原因'),
        ),
        migrations.AlterField(
            model_name='reborn_application',
            name='level',
            field=models.IntegerField(choices=[(2, '高'), (1, '中'), (0, '低')], default=0, verbose_name='严重程度'),
        ),
        migrations.AlterField(
            model_name='reborn_application',
            name='outerlevel',
            field=models.IntegerField(choices=[(2, '3'), (3, '4'), (0, '1'), (1, '2'), (4, '5')], default=0, verbose_name='外部等级'),
        ),
    ]
