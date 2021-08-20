from django.db import models
import shutil
import os
from django.conf import settings

class Image(models.Model):
    image = models.ImageField(upload_to='tmp')

class Feedback(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['created_on']
    
    def __str__(self):
        return 'Feedback {} by {}'.format(self.body, self.name)

