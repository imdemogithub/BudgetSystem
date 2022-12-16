from django.contrib import admin
from .models import *
# Register your models here.

all_models = [Budget, Expense, ExpenseCategory, ExpenseMemberList, Master, ShareExpense, UserProfile]

for model in all_models:
    admin.site.register(model)