from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="할일")
    description = models.TextField(null=True, blank=True, verbose_name="디테일")
    complete = models.BooleanField(default=False, verbose_name="완료여부")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']