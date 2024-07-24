from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Diner(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.diner.name})"

class CustomerOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name='customer_orders')
    items = models.ManyToManyField(MenuItem, related_name='customer_orders')
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f"Order by {self.customer_name} at {self.diner.name}"

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.customer_name} at {self.diner.name} on {self.booking_date} at {self.booking_time}"

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    comment = models.TextField()
    feedback_date = models.DateField()

    def __str__(self):
        return f"Feedback by {self.customer_name} at {self.diner.name} on {self.feedback_date}"

class Supply(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name='supplies')

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit}) for {self.diner.name}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name='employees')
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.position} at {self.diner.name}"
