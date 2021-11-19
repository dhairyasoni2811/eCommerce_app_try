import os
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

"""
    superuser:
        Username: DhairyaSoni
        email: dsdrago27@gmail.com
        Password: Dh@irya2811
"""


# Create your models here.
class User(AbstractUser):
    pass


class Category(models.Model):
    """ this module will store item category. """
    Item_Category = models.TextField()

    def __str__(self):
        return f"{self.pk}. - {self.Item_Category}"


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join("upload/", filename)


class SellItemList(models.Model):
    """ this module will store item details """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="item_to_sell")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product")
    buyers = models.ManyToManyField(User, default=None, blank=True)
    quantity = models.IntegerField(default=1)
    title = models.TextField()
    image_url = models.ImageField(upload_to=filepath, null=True, blank=True)
    description = models.TextField()
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f"""
            Title: {self.title}\n
            Description: {self.description}\n
            Price: ${self.price}\n
            Image URL: {self.image_url}\n
            Quantity: {self.quantity}\n
            Category: {self.category}\n\n\n 
        """


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="i_want_this")
    item = models.ManyToManyField(SellItemList)

    def __str__(self):
        return f"""
            {self.user.username}\n
                \t{self.item}\n\n
        """


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    item = models.ForeignKey(SellItemList, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return f"""
            User: {self.user.username}\n
            Item: {self.item.title}\n
            Comment: {self.comment}\n\n\n
        """
