from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class alumni(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  profile=models.ImageField(upload_to='profile/')
  course=models.CharField(max_length=100)
  startyear=models.IntegerField()
  endyear=models.IntegerField()
  gpa=models.IntegerField()
  # year = models.CharField(max_length=50)

  def __str__(self):
    return self.user.username

  
class experience(models.Model):
  alumni=models.ForeignKey(alumni,on_delete=models.CASCADE)
  companyname=models.CharField(max_length=100)
  year = models.CharField(max_length=50)
    
  def __str__(self):
    return self.companyname +' of '+ self.alumni.user.username

  
class projects(models.Model):
  alumni=models.ForeignKey(alumni,on_delete=models.CASCADE)
  projectname=models.CharField(max_length=100)
  projectdetails=models.TextField()
  link=models.CharField(max_length=200)
  
  def __str__(self):
    return self.projectname + ' of ' + self.alumni.user.username

  
# class skills(models.Model):
#   project=models.ForeignKey(projects,on_delete=models.CASCADE)
#   name=models.CharField()  

class Seminar(models.Model):
    organization_name = models.CharField(max_length=100)
    mentor_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    duration = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.CharField(max_length=200)
    
    def __str__(self):
      return self.mentor_name
    
# class Success(models.Model):
#     alumni = models.ForeignKey(alumni,on_delete=models.CASCADE)  
#     story = models.TextField(max_length=200)

    

  
  
  

