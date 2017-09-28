from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def __str__(self):
        return self.title


class Choice(models.Model):
    # ForeignKey 는 해당 클래스를 지정해주면 된다
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=100)
    votes = models.IntegerField()

    def __str__(self):
        return f'({self.question.title}) - 선택지 ({self.title})'
