# Generated by Django 4.0.3 on 2022-04-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_regform_uniqueid_alter_regform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='regform',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]