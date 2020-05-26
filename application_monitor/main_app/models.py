from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class JobPost(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=300)
    image = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'job_posts'
        managed = True
        verbose_name = 'JobPost'
        verbose_name_plural = 'JobPosts'

    def __str__(self):
        return f"Title : {self.job_title}\n Job Description : {self.job_description}\n Email: {self.email}\nPhone Number: {self.phone}\n publisher: {self.author}"