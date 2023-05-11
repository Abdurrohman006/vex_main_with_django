from django.db import models

# Create your models here.


class Colors(models.Model):
    color = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.color


class Sizes(models.Model):
    size = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.size


class MultipleImage(models.Model):
    images = models.FileField()


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    text = models.TextField(null=True)
    colors = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True, blank=True)
    sizes = models.ForeignKey(Sizes, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ForeignKey(MultipleImage, on_delete=models.SET_NULL, null=True, blank=True)

# [rasm1.jpg, rasm2.png, ]
    def __str__(self):
        return self.name

