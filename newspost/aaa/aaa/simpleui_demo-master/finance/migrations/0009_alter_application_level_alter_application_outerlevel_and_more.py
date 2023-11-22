# Generated by Django 4.1.7 on 2023-07-04 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0028_alter_department_options_alter_title_options_and_more'),
        ('finance', '0008_alter_application_outerlevel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='level',
            field=models.IntegerField(choices=[(0, '低'), (2, '高'), (1, '中')], default=0, verbose_name='严重程度'),
        ),
        migrations.AlterField(
            model_name='application',
            name='outerlevel',
            field=models.IntegerField(choices=[(3, '4'), (0, '1'), (4, '5'), (1, '2'), (2, '3')], default=0, verbose_name='外部等级'),
        ),
        migrations.AlterField(
            model_name='defaultperson',
            name='level',
            field=models.IntegerField(choices=[(0, '低'), (2, '高'), (1, '中')], default=0, verbose_name='严重程度'),
        ),
        migrations.AlterField(
            model_name='defaultperson',
            name='outerlevel',
            field=models.IntegerField(choices=[(3, '4'), (0, '1'), (4, '5'), (1, '2'), (2, '3')], default=0, verbose_name='外部等级'),
        ),
        migrations.AlterField(
            model_name='defaultperson',
            name='rebornreason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.title', verbose_name='重生原因'),
        ),
    ]