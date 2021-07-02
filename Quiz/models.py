from django.db import models

# W tej sekcji tworzone są modele


class Category(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name


class Quizz(models.Model):
    name = models.CharField(max_length=64, null=False)
    category = models.ForeignKey(Category, related_name='quizes', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=128, null=False)
    quizz = models.ForeignKey(Quizz, related_name='questions', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField(max_length=64, null=False)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
