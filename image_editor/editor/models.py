from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image
