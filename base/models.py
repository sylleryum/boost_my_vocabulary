from django.db import models
from django.contrib.auth.models import User
from users.models import NewUser


class Dictionary(models.Model):
    # a better alternative would be to use a table with languages available rather than a string as below.
    language = models.CharField(max_length=50, null=True, blank=True, unique=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "dictionary"


class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, null=True, blank=True)
    word = models.CharField(max_length=200, null=True, blank=True)
    translation = models.CharField(max_length=200, null=True, blank=True)
    data_added = models.DateTimeField()
    last_reviewed = models.DateTimeField()
    times_reviewed = models.IntegerField()
    successful_reviews = models.IntegerField()
    notes = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = "word"
