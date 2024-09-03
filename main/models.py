from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

#single not plural --> tables in code should be single 

class Category(models.Model):
    # name varchar constraints  -->> حدودو اللي هتحطها علي ال column
    name = models.CharField(max_length= 50 , unique=True)
    #what is the Difference between null and blank ?
    description = models.TextField(null = True , blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    #Dunder/Magic Function 
    def __str__(self):
        return self.name
#1
    
# class Tag(models.model):
#     name = models.CharField(max_length=50 )

#     # category = models.ManyToManyField(Category )
#     # tst = models.OneToOneField()


#m
class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING' , 'PENDING'),
        ('IN PROGRESS' , 'IN PROGRESS'),
        ('COMPLETED' , 'COMPLETED'),
    ]
    
    title=models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length = 12 , choices = STATUS_CHOICES , default = 'PENDING')
    priority = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(10)] ,null= True , blank= True) 
    due_date = models.DateField(null= True , blank=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    user = models.ForeignKey(User , on_delete=models.CASCADE)


 
class comment(models.Model):
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)


    task = models.ForeignKey(Task , on_delete = models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)