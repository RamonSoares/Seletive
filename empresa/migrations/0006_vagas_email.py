# Generated by Django 4.1.3 on 2022-11-10 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_alter_vagas_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
