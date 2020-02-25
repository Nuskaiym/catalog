from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField
from smart_selects.db_fields import ChainedForeignKey


class Category(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    is_active = models.BooleanField(default=True)


class Manufacturer(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    photo = ResizedImageField(upload_to='product/', verbose_name='Фотография', size=[1000, 600], max_length=300)
    url = models.URLField(default=None)


class Product(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextUploadingField()
    is_top = models.BooleanField(default=False)
    characteristic = RichTextUploadingField()
    price = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sub_category = ChainedForeignKey(SubCategory, on_delete=models.CASCADE)
                                     # chained_field="category",
                                     # chained_model_field="category",
                                     # show_all=False,
                                     # auto_choose=True,
                                     # sort=True)
