from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + self.last_name
