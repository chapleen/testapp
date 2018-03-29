from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    weight = models.FloatField()
    brand = models.CharField(max_length=128)
    price = models.FloatField()
    expirationDate = models.DateField()
    def __str__(self):
        return "%s-%s" % (self.brand, self.name)


class Store(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    products = models.ManyToManyField(to=Product)
    def __str__(self):
        return "%s(%s)" % (self.name, self.address)
