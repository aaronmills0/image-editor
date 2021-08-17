from django.db import models
import shutil
import os
from django.conf import settings

class Image(models.Model):
    image = models.ImageField(upload_to='tmp')

