from django.db import models
from django.conf import settings
from Author.models import User
# Create your models here.
class Books(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    # author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="content_%(class)s")
    title=models.CharField(max_length=200,null=True)
    Price=models.IntegerField()
    Edition=models.IntegerField()

    class Meta:
        db_table = 'books'
