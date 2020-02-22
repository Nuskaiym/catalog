# Generated by Django 2.0.2 on 2020-02-22 21:29

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('photo', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, max_length=300, quality=0, size=[1000, 600], upload_to='product/', verbose_name='Фотография')),
                ('url', models.URLField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('characteristic', ckeditor_uploader.fields.RichTextUploadingField()),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Category')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='product.Category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.SubCategory'),
        ),
    ]