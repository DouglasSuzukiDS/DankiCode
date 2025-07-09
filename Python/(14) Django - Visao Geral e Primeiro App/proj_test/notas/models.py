from django.db import models

# Create your models here.
class Nota(models.Model):
   title = models.CharField(max_length=255)

   class Meta:
      ordering = ('title',)