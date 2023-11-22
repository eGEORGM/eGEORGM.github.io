# Generated by Django 4.1.7 on 2023-03-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0014_alter_employe_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oemploye',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='住址'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='insurance',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='保险类型'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='leave_time',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='离职日期'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='liudong',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='流口申报'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='pos',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='职位'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='race',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='民族'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='reason',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='离职原因'),
        ),
        migrations.AlterField(
            model_name='oemploye',
            name='study',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='学历'),
        ),
    ]
