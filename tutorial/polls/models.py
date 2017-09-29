from datetime import timedelta, datetime
from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def __str__(self):
        return f'설문조사 ({self.title})'

    def is_recently(self):
        return bool(self.published_date) and \
               (datetime.now() - self.published_date) < timedelta(days=7)

class Choice(models.Model):
    # ForeignKey 는 해당 클래스를 지정해주면 된다
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=100)
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.title} (설문: {self.question.title})'
