from django.db import models
from member.models import User

# Create your models here.


class Post(models.Model):
    post_text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    modify_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(null=True, blank=True)
    comments = models.ManyToManyField('Comment')
    post_like = models.ManyToManyField(User,through='PostLike', related_name='liked_user')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return '{}님께서 {}에 {}을 작성하셨습니다.'.format(self.author, self.post_time, self.post_text)


class Comment(models.Model):
    comments_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments_date = models.DateTimeField(auto_now=True)
    comments_modify_date = models.DateTimeField(auto_now_add=True)
    comments_text = models.TextField()

    def __str__(self):
        return '{}님께서 {}에 {}댓글을 달았습니다.'.format(self.comments_author, self.comments_date, self.comments_text)


class PostLike(models.Model):
    postlike_users = models.ForeignKey(User, on_delete=models.CASCADE)
    postlike_posts = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return '{}님이 {}에 좋아요 누르셨습니다.'.format(self.postlike_users, self.postlike_posts)


class Tag(models.Model):
    tag_text = models.CharField(max_length=25)
