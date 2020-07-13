from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class UserFile(models.Model):
    user = models.ForeignKey(User, related_name="files",on_delete=models.CASCADE)
    filename = models.CharField(max_length=100,unique=True)
    file = models.FileField(upload_to='uploads/')
    slug = AutoSlugField(populate_from='filename')
    created_at = models.DateTimeField(null=True)
    estimation = models.PositiveIntegerField()
    expiration_date = models.DateTimeField(null=True)
    countdown = models.CharField(max_length=100)

    def __str__(self):
        return self.filename

    def get_absolute_url(self):
        return reverse("file_storage:detail",kwargs={'slug':self.slug})
