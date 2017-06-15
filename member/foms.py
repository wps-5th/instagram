from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix','')
        super().__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'put Username',
            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'placeholder': 'put Password',
           }
        )
    )

    # is_valid 를 실행했을 때, Form내부의 모든 field들에 대한
    # 유효성 검증을 실행하는 메서드
    def clean(self):
        # clean()메서드를 실행한 기본결과 dict를 가져옴
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            self.cleaned_data['user']=user
        else:
            raise forms.ValidationError(
                'Login creadntials not valid'
            )