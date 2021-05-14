from django.db import models

# Create your models here.


class Book(models.Model):

# this function let us when we type Book.objects.all().
# to get the objects name instead geting Book object().
    def __str__(self):
        return self.name


# name is a field for book, we say that to django it is char with max_length = 100 char for each book name
    name = models.CharField(max_length=100)
# desc = description
    desc = models.CharField(max_length=300)
    price = models.IntegerField()
