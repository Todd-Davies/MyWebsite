from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    hint = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question
