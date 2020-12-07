from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def post_list(request):
	me = User.objects.get(username = 'superuser')
	posts = Post.objects.filter(author = me)
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})