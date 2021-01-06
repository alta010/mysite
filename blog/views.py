from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

#def index(request):
#    return render(request, 'blog/main.html')
