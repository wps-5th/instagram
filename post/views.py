from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post


# def index(request):
#     return HttpResponse('hello world!')


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)
