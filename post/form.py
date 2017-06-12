from django import forms


class PostCreate(forms.Form):
    author = forms.CharField(max_length=30)
    # # create_date = forms.DateTimeField()
    comment = forms.CharField(max_length=50)
    # # modify_date = forms.DateTimeField()
    # # tags = forms.CharField(max_length=30)
    photo = forms.ImageField()


class PostModify(forms.Form):
    commnet = forms.CharField(max_length=50)