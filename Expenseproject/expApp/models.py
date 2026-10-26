from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES=(
        ("food","food"),
        ("bill","bill"),
        ("fuel","fuel")
    )
    PAYMENT_CHOICES=(
        ("UPI","UPI"),
        ("card","card")
    )
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    owner=models.ForeignKey(User,on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICES,default="food")
    payment=models.CharField(max_length=100,choices=PAYMENT_CHOICES,default="UPI")

    def __str__(self):
        return f"{self.title} - {self.amount}"