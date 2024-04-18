from django.db import models

class Note(models.Model):
    author=models.TextField()
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    isPin=models.BooleanField(default=False)
    id=models.AutoField(primary_key=True)
    primary=models.CharField(max_length=20,null=True)
    secondary=models.CharField(max_length=20,null=True)

    def __str__(self):
        return sefl.title