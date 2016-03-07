from django.db import models
# Create your models here.

class Question(models.Model) :
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User) 
	likes = models.ManyToManyField(User)

class Answer(models.Model) :
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)