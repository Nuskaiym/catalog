from django.db import models

import PIL
from PIL import Image


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider/')
    url = models.URLField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = Slider.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()

        except:
            pass

        super(Slider, self).save(*args, **kwargs)
        img = Image.open(self.image)
        width, height = img.size
        if width > 1920:
            ratio = float(width / 1920)
            width = int(width / ratio)
            height = int(height / ratio)
            img = img.resize((width, height), PIL.Image.ANTIALIAS)
            img.save(self.image.path, quality=100, optimize=True)
        else:
            img.save(self.image.path, quality=100, optimize=True)
