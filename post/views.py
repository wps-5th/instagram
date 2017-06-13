<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from member.models import User
from post.form import PostCreate, PostModify
from .models import Post

# def index(request):
#     return HttpResponse('hello world!')

User = get_user_model()

=======
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post


# def index(request):
#     return HttpResponse('hello world!')

>>>>>>> origin/master

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)
<<<<<<< HEAD


def post_detail(request, post_pk):
    # post_pk 에 해당하는 Post 객체를 리턴
    posts = Post.objects.get(post_pk=post_pk)
    context = {
        'posts': posts
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    # POST 요청을 받아 Post 객체를 생성 후 post_list 페이지로 redirect
    if request.method == 'GET':
        form = PostCreate()
        context = {
            'form': form,
        }
        return render(request, 'post/post_create.html', context)

    elif request.method == 'POST':
        form = PostCreate(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.first()
            Post.objects.create(
                author=user,
                photo=request.FILES['photo'],
            )
            return redirect('post/post_create.html')
        else:
            context = {
                'form': form,
            }
            return render(request, 'post/post_list.html', context)


def post_modify(request, post_pk):
    # 수정
    post = Post.objects.get(id=post_pk)
    if request.method == 'GET':
        form = PostModify()
        context = {
            'form': form,
        }
        return render(request, 'post/post_modify.html', context)
    elif request.method == 'POST':
        form = PostModify(request.POST, request.FILES)
        if form.is_valid():
            post.photo = request.FILES['photo']
            return redirect('detail', post.pk)


def post_delete(request, post_pk):
    # post_pk 에 해당하는 Post에 대한 delete 요청만 받음
    # 처리완료후에는 post_list 페이지로 redirect
    pass


def comment_create(request, post_pk):
    # POST 요청을 받아 Comment 객체를 생성 후 post_detail 페이지로 redirect
    pass


def comment_modify(request, post_pk):
    # 수정
    pass


def comment_delete(request, post_pk, comment_pk):
    # Post요청을 받아 commnet 객체를 delete, 이후 post_detail페이지로 redirect
    pass
=======
>>>>>>> origin/master
