# core/serializers.py

from rest_framework import serializers
from .models import Account, Transaction, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountDetailSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = "__all__"
        depth = 1  # Include related objects up to one level deep
