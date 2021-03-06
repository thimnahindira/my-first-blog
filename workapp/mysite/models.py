from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CPF = models.IntegerField(max_length=20)
    Endereço = models.CharField(max_length=200)
    Profissão = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title