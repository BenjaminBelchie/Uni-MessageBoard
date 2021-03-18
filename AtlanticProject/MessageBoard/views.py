from django.shortcuts import render, get_object_or_404
from .models import Post
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.db.models import Q
 
#Function to render the Home HTML template and the posts which are objects
def home(request):
	context = {'posts':Post.objects.all()}
	return render(request, 'MessageBoard/home.html',context) 

#Using a list view to see the posts, this is the most suitable order to show the posts as modern desin for message boards/ social media show posts in a list rather than a grid
class PostListViewD(LoginRequiredMixin, ListView): #I used a class structure as its more efficant and the core functionality is handled for me, I only have to define the varibles.
	model = Post #Defining the model as a post
	template_name = 'MessageBoard/home.html' #Assigning the template to the correct HTML file
	context_object_name = 'posts' #Giving the object a name
	ordering = ['-datePosted'] #Ordering the posts by date posted as default so newest posts will be shown first.
	paginate_by = 5 #Setting it so only 5 posts are shown per page

	def searchBar(request):
		if request.GET:
			query = request.GET['q']
			context['query']=str(query)

class PostListViewA(LoginRequiredMixin, ListView): #I used a class structure as its more efficant and the core functionality is handled for me, I only have to define the varibles.
	model = Post #Defining the model as a post
	template_name = 'MessageBoard/home.html' #Assigning the template to the correct HTML file
	context_object_name = 'posts' #Giving the object a name
	ordering = ['datePosted'] #Ordering the posts by date posted as default so newest posts will be shown first.
	paginate_by = 5 #Setting it so only 5 posts are shown per page.

class UserPostListView(LoginRequiredMixin, ListView): #This is very simular to the main posts view but this is setting the method to view the posts made by one author.
	model = Post #Defining the model as post
	template_name = 'MessageBoard/user_posts.html' #Assigning the template the right HTML file
	context_object_name = 'posts' #giving the object a name
	paginate_by = 5 #Also setting there to be 5 posts per page so design is consistant across all areas of the app

	def get_queryset(self): #Function to ensure that the user has posts
		user = get_object_or_404(User, username=self.kwargs.get('username')) #This assigns the user varible a method that either results in a 404 if the user doesnt exist or it will show all the posts made by that user.
		return Post.objects.filter(author=user).order_by('-datePosted') #Odering the posts by most recent too

class PostDetailView(DetailView): #The method to view individual posts
	model = Post

class UserListAll(ListView): #Method to list all the Authors, used to filter by author
	model = Profile #Setting the model to Profile
	template_name = 'MessageBoard/users_list.html' #Assigning the template to the method

def get_queryset(request, query=None): #Method to search for posts
	queryset= [] #Creating a list for the query to be sored in
	queries = query#Splitting the input by spaces
	for q in queries: #Creating a loop to constantly loop over the query
		posts = Post.objects.filter( #Setting the filters up for search
			Q(title__icontains=q), #Show results that match the title
			Q(content__icontains=q) #Show results thar match the content
			)
		for post in posts: #Looping over the results
			queryset.append(post) #Show the post
	return list(set(queryset))#Returning the query


class PostCreateView(LoginRequiredMixin, CreateView): #The method to create a post
	model = Post #Assigning the model post
	fields = ['title', 'content'] #Specifying the fields that I want to appear on the form

	def form_valid(self, form): #Function to ensure that the form is valid
		form.instance.author= self.request.user #Checking that the author creating the post is the user signed in
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):#Method to update posts
	model = Post #Assigning the model post
	fields = ['title', 'content'] #Specifying the fields that need to be on the form

	def form_valid(self, form): #Again checking if the form is valid
		form.instance.author= self.request.user #Also checking if the user updating the post is the user signed in
		return super().form_valid(form)

	def test_func(self):#More validation to check if the user making the request is the user who owns the post
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#Setting the delete method
	model = Post
	success_url = '/MessageBoard'#Sending users to a url if the post deletion is sucsessful

	def test_func(self): #The same vslidation as earlier to check if the logged in user is the user that owns that post 
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	


    
@login_required
def about(request):
	return render(request, 'MessageBoard/about.html',{'title':'About'})













