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
        related_name='like_posts',
        through='PostLike',
    )
    tags = models.ManyToManyField(
        'Tag',
    )

    def add_comment(self, user, content):
        return self.comment_set.create(author=user, content=content)

    def add_Tag(self, tag_name):
        tag, tag_created = Tag.objects.get_or_create(name=tag_name)
        if not self.tags.filter(name=tag_name).exists():
            self.tags.add(tag)

    @property
    def like_count(self):
        return self.like_users.count()


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    like_users = models.ManyToManyField(
        User,
        through='CommentLike',
        related_name='like_comments',
    )


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'post_post_like_users'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
