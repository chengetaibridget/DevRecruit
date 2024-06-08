from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    firstname=models.CharField(max_length=500)
    lastname=models.CharField(max_length=500)
    phone=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    employmentprogress=models.IntegerField(default=0)
    education=models.CharField(max_length=500)
    institute=models.CharField(max_length=500)
    profession=models.CharField(max_length=500,default="Engineer")

class Practical(models.Model):
      creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='crtr')
      date_created=models.DateField(default=timezone.now)
      test_number=models.IntegerField()
      test_title=models.CharField(max_length=100)
      test_name=models.CharField(max_length=200)
      test_details=models.TextField()
      expected_result=models.TextField()
      mark=models.IntegerField()


class Answer(models.Model):
     practical_test=models.ForeignKey(Practical,on_delete=models.CASCADE,related_name='prac')
     candidate=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cand')
     date_created=models.DateField(default=timezone.now)
     solution=models.TextField()
     candidate_result=models.TextField()
     score=models.IntegerField(default=0)

     #(1, 2024-02-16, print("hey"), hey, 10, 2, null)

class Theorytest(models.Model):
      creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
      date_created=models.DateField(default=timezone.now)
      question=models.TextField()
      option1=models.CharField(max_length=100,null=True)
      option2=models.CharField(max_length=100,null=True)
      option3=models.CharField(max_length=100,null=True)
      option4=models.CharField(max_length=100,null=True)
      answer=models.CharField(max_length=100,null=True)

class Progress(models.Model):
     engineer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='eng')
     scorebar=models.IntegerField(default=0)
     hired=models.BooleanField(default=False)
     elligible=models.BooleanField(default=False)

     

