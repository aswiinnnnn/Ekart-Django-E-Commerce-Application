# Generated by Django 4.2.21 on 2025-06-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='size',
            field=models.IntegerField(choices=[(1, 'Small'), (2, 'Medium'), (3, 'Large'), (4, 'X-Large'), (5, 'XX-Large')], default=2),
        ),
    ]
