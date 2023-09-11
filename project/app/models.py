from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ch = (
    (1, 'male'), (2, 'female'), (3, 'unisex')
)
ch2 = (
    (1, 'smartwatch'), (2, 'dailwatch')
)


class Gallary(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    ColorName = models.CharField(max_length=50)
    Gender = models.IntegerField(choices=ch, null=True)
    Quantity = models.IntegerField(null=True)
    Category = models.IntegerField(choices=ch2, null=True)
    # Color=models.CharField()
    Image = models.ImageField(upload_to='productimages')



class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_id = models.IntegerField()
    purchased_quan = models.IntegerField()
    date = models.DateField(auto_now_add=True)
