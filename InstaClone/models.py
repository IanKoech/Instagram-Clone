from django.db import models

# Create your models here.
class Image(models.Model):
    '''
    Class creates columns in the image table
    '''
    name = models.CharField(max_length = 30)
    caption = models.CharField(max_length = 30)
    
    