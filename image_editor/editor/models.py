from django.db import models
import shutil
import os
from django.conf import settings

class Image(models.Model):
    shutil.rmtree('{}\\tmp'.format(settings.MEDIA_ROOT[:-1]))
    os.mkdir('{}\\tmp'.format(settings.MEDIA_ROOT[:-1]))
    image = models.ImageField(upload_to='tmp')

