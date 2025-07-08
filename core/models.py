# core/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Puedes agregar campos extra aquí si lo deseas
    phone = models.CharField(max_length=20, blank=True)
    pass


class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=10, default="CLP")  # o USD, EUR, etc.

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class Category(models.Model):
    TYPE_CHOICES = [
        ("income", "Ingreso"),
        ("expense", "Gasto"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.type})"


class Transaction(models.Model):
    TYPE_CHOICES = [
        ("income", "Ingreso"),
        ("expense", "Gasto"),
    ]
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}: {self.amount} on {self.date}"


class RecurringTransaction(models.Model):
    FREQUENCY_CHOICES = [
        ("weekly", "Semanal"),
        ("monthly", "Mensual"),
        ("yearly", "Anual"),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    type = models.CharField(max_length=10, choices=Transaction.TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} recurrente cada {self.frequency}"
