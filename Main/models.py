from django.db import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    tutor = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    rating = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.id} - Rating: {self.rating}'
