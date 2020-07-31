from django.db import models


class SearchHistory(models.Model):
    activity = models.CharField(max_length=300)
    activity_type = models.CharField(max_length=100)
    activity_key = models.CharField(max_length=10)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity
