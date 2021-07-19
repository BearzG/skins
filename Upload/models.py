from django.db import models

# Create your models here.
class Store_skins(models.Model):
    Author = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Image = models.ImageField(upload_to='Skins')

    def __str__(self):
        return 'Image by ' + self.Author