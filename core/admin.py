# core/admin.py

from django.contrib import admin
from .models import Account, Category, Transaction, RecurringTransaction,CustomUser

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(RecurringTransaction)
admin.site.register(CustomUser)
