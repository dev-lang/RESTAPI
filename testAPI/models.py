from django.db import models

# Create your models here.


class Item(models.Model):
    ItemID = models.IntegerField()
    ItemName = models.CharField(max_length=200)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Category = models.CharField(max_length=200)

    def __str__(self):
        return self.ItemName
