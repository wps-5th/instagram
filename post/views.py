from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from member.models import User
from post.form import PostCreate, PostModify
from .models import Post

# def index(request):
#     return HttpResponse('hello world!')

User = get_user_model()


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    # 가져오는 과정에서 예외처리를 한다 (Model.DeosNotExist)
    try:
        post = Post.objects.get(pk=post_pk)
    except Post.DoesNotExist as e:
        # return HttpResponseNotFound(‘Post not found, detail: {}‘.format(e))
        # return redirect('post:post_list')

        url = reverse('post:post_list')
        return HttpResponseRedirect(url)  # 위에 쓴 return redirect 와 같은 의미

        # render함수는 django.template.loader.get_template함수와
        # django.http.HttpResponse함수를 축약해 놓은 shortcut이다

        # Django가 템플릿을 검색할 수 있는 모든 디렉토리를 순회하며
    # 인자로 주어진 문자열값과 일치하는 템플릿이 있는 지 확인 후
    # 결과를 리턴 (django.template.backends.dkango.Template
    template = loader.get_template('post/post_detail.html')

    # dict형 변수 context ‘post’키에 post(Post 객체를 할당
    context = {
        'post': post,
    }

    rendered_string = template.render(context=context, request=request)
    return HttpResponse(rendered_string)


def post_create(request):
    # POST 요청을 받아 Post 객체를 생성 후 post_list 페이지로 redirect
    # if request.method == 'GET':
    #     form = PostCreate()
    #     context = {
    #         'form': form,
    #     }
    #     return render(request, 'post:post_create.html', context)
    #
    # elif request.method == 'POST':
    #     form = PostCreate(request.POST, request.FILES)
    #     if form.is_valid():
    #         user = User.objects.first()
    #         Post.objects.create(
    #             author=user,
    #             photo=request.FILES['photo'],
    #         )
    #         return redirect('post:post_create.html')
    #     else:
    #         context = {
    #             'form': form,
    #         }
    #         return render(request, 'post:post_list.html', context)

    if request.method == 'POST':
        user = User.objects.first()
        post = Post.objects.create(
            author=user,
            photo=request.FILES['file']
        )
        comment_string = request.POST.get('comment', '')
        if comment_string:
            post.comment_set.create(
                author=user,
                content=comment_string,
            )
        return redirect('post:post_detail', post_pk=post.pk)
    else:
        return render(request, 'post/post_create.html')


def post_modify(request, post_pk):
    # 수정
    post = Post.objects.get(id=post_pk)
    if request.method == 'GET':
        form = PostModify()
        context = {
            'form': form,
        }
        return render(request, 'post:post_modify.html', context)
    elif request.method == 'POST':
        form = PostModify(request.POST, request.FILES)
        if form.is_valid():
            post.photo = request.FILES['photo']
            return redirect('post_detail', post.pk)


def post_delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        post.delete()
    return redirect('post:post_list')


def comment_create(request, post_pk):
    # POST 요청을 받아 Comment 객체를 생성 후 post_detail 페이지로 redirect
    pass


def comment_modify(request, post_pk):
    # 수정
    pass


def comment_delete(request, post_pk, comment_pk):
    # Post요청을 받아 commnet 객체를 delete, 이후 post_detail페이지로 redirect
    pass
