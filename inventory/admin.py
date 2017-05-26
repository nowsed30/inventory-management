from django.contrib import admin

# import our Item model
from .models import Item


# add a custom Model class for admin Page
class ItemAdmin(admin.ModelAdmin):
    # fields of the items to be displayed
    list_display = ['item', 'amount']

# register this Item model with django admin site
admin.site.register(Item, ItemAdmin)
