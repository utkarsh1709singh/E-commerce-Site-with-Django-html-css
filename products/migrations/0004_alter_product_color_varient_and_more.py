# Generated by Django 4.2.2 on 2023-10-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_colour_name_colorvarient_color_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_varient',
            field=models.ManyToManyField(blank=True, to='products.colorvarient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_varient',
            field=models.ManyToManyField(blank=True, to='products.sizevarient'),
        ),
    ]
