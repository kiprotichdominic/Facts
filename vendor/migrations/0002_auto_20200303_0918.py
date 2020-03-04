# Generated by Django 2.2.10 on 2020-03-03 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='category',
        ),
        migrations.AddField(
            model_name='vendor',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vendor.Products'),
            preserve_default=False,
        ),
    ]