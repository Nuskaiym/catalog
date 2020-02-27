from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django_resized import ResizedImageField
from smart_selects.db_fields import ChainedForeignKey

import PIL
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='manufacturer/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = Manufacturer.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()

        except:
            pass

        super(Manufacturer, self).save(*args, **kwargs)
        img = Image.open(self.image)
        width, height = img.size
        if width > 800:
            ratio = float(width / 800)
            width = int(width / ratio)
            height = int(height / ratio)
            img = img.resize((width, height), PIL.Image.ANTIALIAS)
            img.save(self.image.path, quality=100, optimize=True)
        else:
            img.save(self.image.path, quality=100, optimize=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextUploadingField()
    is_top = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    characteristic = RichTextUploadingField()
    price = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sub_category = ChainedForeignKey(SubCategory, chained_model_field='Category', show_all=True, auto_choose=False)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = Product.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()

        except:
            pass

        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image)
        width, height = img.size
        if width > 800:
            ratio = float(width / 800)
            width = int(width / ratio)
            height = int(height / ratio)
            img = img.resize((width, height), PIL.Image.ANTIALIAS)
            img.save(self.image.path, quality=100, optimize=True)
        else:
            img.save(self.image.path, quality=100, optimize=True)


@receiver(pre_delete, sender=Product)
def delete_image(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

    # chained_field="category",
    # chained_model_field="category",
    # show_all=False,
    # auto_choose=True,
    # sort=True)
