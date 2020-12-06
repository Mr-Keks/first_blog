from django.shortcuts import render
from .models import Post
from django.utils import timezone 
from django.contrib.auth.models import User

def post_list(request):
	me = User.objects.get(username = 'superuser')
	posts = Post.objects.filter(author = me)
	return render(request, 'blog/post_list.html', {'posts':posts})
