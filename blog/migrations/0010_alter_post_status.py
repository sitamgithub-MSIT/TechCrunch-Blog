# Generated by Django 4.2.2 on 2023-10-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('active', 'Active')], default='draft', max_length=20),
        ),
    ]
