# Generated by Django 4.1.7 on 2023-04-09 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
