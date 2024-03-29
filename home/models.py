from django.db import models
from django.utils import timezone
# from django.core.validators import MinLengthValidator
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.urls import reverse

class Post(models.Model) :
    title = models.CharField(max_length=200)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_owner')
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # recording the timestamp when a new entry is created
    # author = models.ForeignKey(User, on_delete=models.CASCADE ) # ForeignKey defines a "many-to-one relationship"
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})