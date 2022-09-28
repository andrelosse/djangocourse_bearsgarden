from unittest.util import _MAX_LENGTH
from django.db import models

class Size (models.Model):

    size = models.CharField(max_length=7)

    def __str__ (self):
        return self.size

class Pizza (models.Model):

    topping1 = models.CharField(max_length=17)
    topping2 = models.CharField(max_length=17)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)