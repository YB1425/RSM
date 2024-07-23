from django.contrib import admin
from .models import *

admin.site.register(Staff)
admin.site.register(Ingredient)
admin.site.register(Review)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Restaurant)