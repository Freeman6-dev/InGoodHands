from django.db import models


# Create your models here.
from InGoodHands import settings


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"



class Institution(models.Model):
    FOUNDATION = 1
    NON_GOVERNMENTAL_ORGANIZATION = 2
    LOCAL_COLLECTION = 3
    TYPE_CHOICES = [
        (FOUNDATION, 'Fundacja'),
        (NON_GOVERNMENTAL_ORGANIZATION, 'Organizacja pozarządowa'),
        (LOCAL_COLLECTION, 'Zbiórka lokalna')
    ]
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES, default=FOUNDATION)
    categories = models.ManyToManyField(Category, related_name='institutions')

    def categories_list(self):
        list = []
        for element in self.categories.values():
            list.append(element['name'])
        return ', '.join([str(elem) for elem in list])


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='donations')
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=15)
    pick_up_date = models.DateField(null=True, blank=True)
    pick_up_time = models.TimeField(null=True, blank=True)
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
