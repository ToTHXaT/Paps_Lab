# Generated by Django 3.0.6 on 2020-05-23 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='pass_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='sup_dep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.Department'),
        ),
    ]