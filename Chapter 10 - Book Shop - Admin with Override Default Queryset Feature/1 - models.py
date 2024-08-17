from django.db import models

class Category(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)

    description = models.TextField()

    article_count = models.IntegerField()

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'