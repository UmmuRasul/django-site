from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    Date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

        #use reverse fns coz we want to return de for url as a string and the view will handle the redirect fns 

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk}) #post-detail is de for path
