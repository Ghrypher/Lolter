# Generated by Django 4.1.2 on 2022-10-12 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_champ_rol_champrol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='champ',
            old_name='name',
            new_name='nombre',
        ),
    ]