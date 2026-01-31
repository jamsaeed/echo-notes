from django.db import models
from django.urls import reverse
#from datetime import datetime
# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200)
    note_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"note_id": self.pk})


