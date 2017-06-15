from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from member.models import User
from post.models import Post


def login(request):
    # member/login.html 생성
    # username, password, button 이 있는 HTML 생성
    # POST 요청이 올 경우 좌측 코드를 기반으로 로그인 완료 후 post_list로 이동
    # 실패할 경우 HttpResponse로 'Login invalid' 띄어주기

    # username = User.objects.get()
    # password = User.objects.get()
    if request.method == 'POST':

        return redirect('post:post_list')
    else:
        return render(request, 'member/login.html')