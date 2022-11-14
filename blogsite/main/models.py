from django.db import models

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default='user')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
