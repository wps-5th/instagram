from django.contrib.auth import authenticate, login as django_login, logout as django_logout, get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from member.models import User
# from post.models import Post
from member.models import User

User = get_user_model()


def login(request):
    # member/login.html 생성
    # username, password, button 이 있는 HTML 생성
    # POST 요청이 올 경우 좌측 코드를 기반으로 로그인 완료 후 post_list로 이동
    # 실패할 경우 HttpResponse로 'Login invalid' 띄어주기

    # username = request.User.get('User','')
    # password = User.objects.get()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            django_login(request, user)
            return redirect('post:post_list')
        else:
            return HttpResponse('Login credentials invalid')
    else:
        if request.user.is_authenticated:
            return redirect('post:post_list')
        return render(request, 'member/login.html')


def logout(request):
    django_logout(request)
    return redirect('post:post_list')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            return HttpResponse('다른 이름을 사용하세요')

        elif password1 != password2:
            return HttpResponse('비밀번호가 동일하지 않습니다.')
        user = User.objects.create_user(
            username=username,
            password=password1,
        )
        django_login(request, user)
        return redirect('post:post_list')
    else:
        return render(request, 'member/signup.html')
