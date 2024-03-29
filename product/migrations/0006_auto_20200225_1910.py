# Generated by Django 2.0 on 2020-02-25 19:10

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200225_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_model_field='Category', on_delete=django.db.models.deletion.CASCADE, to='product.SubCategory'),
        ),
    ]
