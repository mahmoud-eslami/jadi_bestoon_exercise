# Generated by Django 3.0.6 on 2020-05-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200509_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('mn', 'man'), ('wn', 'woman')], default='mn', max_length=2),
        ),
    ]