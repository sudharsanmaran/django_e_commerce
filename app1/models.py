from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=200)
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name




class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,related_name='products',
                               on_delete=models.CASCADE)
    price=models.FloatField()
    image=models.ImageField(upload_to='images/')
    is_available=models.BooleanField(default=True)
    user = models.ManyToManyField(User, blank=True,null=True)

    def __str__(self):
        return self.name






