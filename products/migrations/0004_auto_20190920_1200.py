# Generated by Django 2.2.4 on 2019-09-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Additionals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_product', models.CharField(max_length=30)),
                ('ad_price', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='additionals',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='food_region',
            field=models.CharField(max_length=30),
        ),
    ]
