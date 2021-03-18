from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#I am using a class based Post Model as its more efficant, I can only write the extra code, all the core functionality and behavour of the posts are defined in the model
class Post(models.Model):
	title = models.CharField(max_length=100) #Setting the fields for the posts
	content = models.TextField() #Setting the fields for the post
	datePosted = models.DateTimeField(default=timezone.now) #Making the date stamp for the posts, it defaults to the current date/ time so it autmomatically tags posts with the right date
	author = models.ForeignKey(User, on_delete=models.CASCADE) #Assigning the user varible to the author section of a post, I also added .CASCADE to ensure if a user is deleted so is thier posts

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})


