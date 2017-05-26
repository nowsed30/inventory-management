from django.db import models


# Models are inherited from models.Model
# FirstModel : Item
class Item(models.Model):
    # item title, a char field
    item = models.CharField(max_length=200)
    # description field, a text field
    description = models.TextField()
    # amount : an integer field
    amount = models.IntegerField()
