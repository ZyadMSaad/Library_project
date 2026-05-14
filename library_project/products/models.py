from django.db import models

# Create your models here.

class Product(models.Model):
  
     # book name
    name = models.CharField(max_length=100)
    
   
    book_id = models.IntegerField(unique=True)
    
  
    CATEGORY_CHOICES = [
      ('fantase','fantase'),
       ('romance','romance'),
       ('Action','Action'),
       ('History','History'),
       ('Religious','Religious'),
         ('Science','Science'),
         ('Horror','Horror'),
         ('Other','Other'),
  
  
    ]
    FORMAT_CHOICES =[
        ('E-book','E-book'),
        ('Hardcopy','Hardcopy'),
    ]
    # category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    

    # author = models.CharField(max_length=100)
    

    # description = models.TextField(null=True,blank=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    language = models.CharField(max_length=100 ,default='English')

    author = models.CharField(max_length=100)
    active=models.BooleanField(default=True, verbose_name='Active')

    format = models.CharField(max_length=50, choices= FORMAT_CHOICES, default='Hardcopy')
    image=models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    borrowed = models.BooleanField(default=False)
    

class Borrow(models.Model):
    

    borrow_date= models.DateField(auto_now_add=True)
    
    user_name =models.CharField(max_length=100)
    
    user_id = models.IntegerField(unique=True)
    
    book_id = models.IntegerField(unique=True)
    
    return_date= models.DateField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name ="borrow"       
  