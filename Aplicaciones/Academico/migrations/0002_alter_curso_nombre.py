# Generated by Django 4.0 on 2022-02-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=55),
        ),
    ]