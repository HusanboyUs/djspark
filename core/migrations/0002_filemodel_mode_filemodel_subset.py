# Generated by Django 4.2.2 on 2023-06-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='mode',
            field=models.CharField(choices=[('ALL', 'ALL'), ('ANY', 'ANY')], default='Choose Mode', max_length=40),
        ),
        migrations.AddField(
            model_name='filemodel',
            name='subset',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
