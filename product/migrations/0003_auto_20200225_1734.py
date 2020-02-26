# Generated by Django 2.0 on 2020-02-25 17:34

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200222_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=smart_selects.db_fields.ChainedForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SubCategory'),
        ),
    ]