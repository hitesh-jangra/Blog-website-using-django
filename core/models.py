from django.db import models
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Question(models.Model):
    ques=models.CharField(max_length=500)
    pub_date=models.DateTimeField('Date Published',auto_now_add=True)

    def __str__(self):
        return self.ques

    def get_absolute_url(self):
        return reverse('view_question',kwargs={"id":self.id})

class Answer(models.Model):
    ques=models.ForeignKey(Question,on_delete=models.CASCADE,default=False)
    ans=models.TextField()
    pub_date=models.DateTimeField('Date Answered',auto_now_add=True)

    def __str__(self):
        return self.ans

class Blog(models.Model):
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    content=RichTextUploadingField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('visitblog',kwargs={"id":self.id})


    