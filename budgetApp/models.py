from django.db import models
import datetime

# creating month choices
month_choices = []

for m in range(1, 13):
    d = datetime.date(2022, m, 1)
    pair = (m, d.strftime("%B"))
    month_choices.append(pair)

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'
    
    def __str__(self) -> str:
        return self.Email

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)

class UserProfile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to="user_profiles/", default="user.png")

    UserName = models.CharField(unique=True, max_length=20)
    FullName = models.CharField(max_length=20, default='', blank=True, null=True)
    Gender = models.CharField(choices=gender_choices, max_length=20, default='', blank=True, null=True)
    BirthDate = models.DateField(default='2022-11-01', blank=True, null=True)
    Address = models.TextField(max_length=150, default='', blank=True, null=True)

    class Meta:
        db_table = 'UserProfile'
    
    def __str__(self) -> str:
        return self.UserName

class ExpenseCategory(models.Model):
    IconImage = models.FileField(upload_to="exp_categories", default="icon.png")
    Category = models.CharField(max_length=50)

    class Meta:
        db_table = 'ExpenseCategory'
    
    def __str__(self) -> str:
        return self.Category

class Budget(models.Model):
    # ExpenseCategory = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    BudgetMonth = models.CharField(choices=month_choices, max_length=10)
    BudgetAmount = models.FloatField()

    class Meta:
        db_table = 'Budget'

    def __str__(self) -> str:
        return self.UserProfile.FullName

class Expense(models.Model):
    ExpenseImage = models.FileField(upload_to="expense_images/", default="user.png")
    ExpenseCategory = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    ExpenseDate = models.DateTimeField(auto_created=True)
    Amount = models.FloatField()
    Description = models.TextField(max_length=255)

    class Meta:
        db_table = 'Expense'
    
    def __str__(self) -> str:
        return self.UserProfile.FullName

class ExpenseMemberList(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ListTitle = models.CharField(max_length=50)
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # for another user reference

class ShareExpense(models.Model):
    ExpenseMemberList = models.ForeignKey(ExpenseMemberList, on_delete=models.CASCADE)
    ExpenseImage = models.FileField(upload_to="expense_images/", default="user.png")
    ExpenseCategory = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    ExpenseDate = models.DateTimeField(auto_created=True)
    Amount = models.FloatField()

    class Meta:
        db_table = 'ShareExpense'

    def __str__(self) -> str:
        return self.Master.Email
