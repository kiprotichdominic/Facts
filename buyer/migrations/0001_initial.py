# Generated by Django 2.2.10 on 2020-03-04 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Name', models.CharField(max_length=200)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='buyer.buyer')),
            ],
        ),
    ]