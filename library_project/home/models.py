from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    # كمل باقي الحقول اللي معاك في البروجيكت التاني

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField()