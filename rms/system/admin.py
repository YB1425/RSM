from django.contrib import admin
from .models import CustomUser, Employee, Supply, Feedback, Booking, CustomerOrder, MenuItem, Diner

admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Supply)
admin.site.register(Feedback)
admin.site.register(Booking)
admin.site.register(CustomerOrder)
admin.site.register(MenuItem)
admin.site.register(Diner)
