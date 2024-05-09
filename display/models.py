from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from email.policy import default
from unicodedata import category
from django.db import models
from datetime import datetime
from  accounts.models import UserProfile



class Display(models.Model) :
    url=models.URLField(unique=True)
    text = models.CharField(max_length=150) 
    isyoutube=models.BooleanField(default=True)
    
class  Display_Data(models.Model) :
         displays = models.ForeignKey(Display,on_delete=models.CASCADE,default=1)  
         users= models.ManyToManyField(UserProfile,default=1)
         choosenum=models.IntegerField()
         puplish_date =models.DateTimeField(default=datetime.now) 
class Meta:
        ordering =['-puplish_date']

    
    