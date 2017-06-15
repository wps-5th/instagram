from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from member.models import User
# from post.models import Post


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
