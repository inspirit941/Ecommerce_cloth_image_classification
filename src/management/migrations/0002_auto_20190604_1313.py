# Generated by Django 2.1.2 on 2019-06-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='pid',
        ),
        migrations.AlterField(
            model_name='product',
            name='sid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
