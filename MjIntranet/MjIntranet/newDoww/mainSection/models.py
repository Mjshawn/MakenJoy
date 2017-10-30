from django.db import models
from django.contrib.auth.models import User
from django.conf import settings






class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length = 100)
    contents = models.TextField()
    select = models.CharField(max_length = 50,
                                       choices = (
                                           ('장고', '장고'),
                                           ('자스', '자스'),
                                           ('제이쿼리','제이쿼리'),
                                           ('django', 'django')
                                       ))
    picture = models.ImageField(blank = True, upload_to="mainSection")
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Member)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length = 100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
