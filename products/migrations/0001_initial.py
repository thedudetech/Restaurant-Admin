# Generated by Django 2.2.4 on 2019-08-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_photo', models.ImageField(height_field=120, upload_to='image', width_field=100)),
                ('product_type', models.CharField(choices=[('Starter', 'STARTERS'), ('Main Course', 'MAIN COURSE'), ('Dessert', 'DESSERT')], max_length=30)),
                ('food_region', models.CharField(choices=[('Panjabi', 'PANJABI'), ('Chinese', 'CHINESE'), ('South Indian', 'SOUTH INDIAN'), ('Kathiyawadi', 'KATHIYAWADI')], max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('product_details', models.CharField(max_length=250)),
                ('product_quantity', models.CharField(max_length=12)),
                ('product_price', models.CharField(max_length=12)),
            ],
        ),
    ]