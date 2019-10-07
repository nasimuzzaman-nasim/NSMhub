from django.db import models
from django.contrib.auth.models import User


# class PostUser(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postuser", null=True)
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name


class Blog(models.Model):
    # postuser = models.ForeignKey(PostUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=2055)
    time = models.DateTimeField(auto_now=True)
    post = models.TextField()
    user = models.CharField(max_length=255, null=True)
    empty = models.IntegerField(default=1)

    def __str__(self):
        return self.title




