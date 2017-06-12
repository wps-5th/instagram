from django.db import models


from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True)
    like_users = models.ManyToManyField(
        User,
        related_name = 'like_posts',
    )
    tags = models.ManyToManyField(
        'Tag',

    )


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    text = models.TextField()


# class PostLike(models.Model):
#     # postlike_users = models.ForeignKey(User, on_delete=models.CASCADE)
#     # postlike_posts = models.ForeignKey(Post,on_delete=models.CASCADE)
#     pass


class Tag(models.Model):
    tag_text = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
