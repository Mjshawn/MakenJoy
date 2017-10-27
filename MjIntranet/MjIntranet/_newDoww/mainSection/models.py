from django.db import models
from django.forms import ValidationError






class Member(models.Model):
    author = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    contents = models.TextField()
    select = models.CharField(max_length = 50,
                                       choices = (
                                           ('장고', '장고'),
                                           ('자스', '자스'),
                                           ('제이쿼리','제이쿼리'),
                                           ('django', 'django')
                                       ))
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
