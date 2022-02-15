from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
