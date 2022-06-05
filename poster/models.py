from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


""""
image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)



This will store the images in date archives like MEDIA_ROOT/users/2020/04/12
"""
