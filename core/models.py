from django.db import models

# Create your models here.
class Question(models.Model):
  Name = models.CharField(max_length=300)
  Email = models.CharField(max_length=300)
  Message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.Name