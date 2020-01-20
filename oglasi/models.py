from django.db import models
from django.urls import reverse

class Oglas(models.Model):
    publisher = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    picture = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000,default='')
    price = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('oglasi:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.publisher + ' - ' + self.title
