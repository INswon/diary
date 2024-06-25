from django.db import models

class Diary(models.Model):

    class Meta:
        db_table = 'day'

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return  self.title