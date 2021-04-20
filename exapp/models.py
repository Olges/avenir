from django.db import models
from django.contrib.auth.models import User

class content(models.Model):
    title = models.CharField(max_length=200, help_text="Enter title of content")
    image = models.ImageField(upload_to='content')
    description = models.TextField(blank = True)
    draft = models.BooleanField(default=True)
    content_type = models.CharField(max_length=200)

class reviews(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text="Enter user name", default='')
    firstname = models.CharField(max_length=200, help_text="Enter user firstname", default='')
    e_mail = models.EmailField(max_length=254, default='')
    message = models.TextField(blank = True)

# def get_absolute_url(self):
#     return reverse('model-detail-view', args=[str(self.id)])

def __str__(self):
    return self.field_name