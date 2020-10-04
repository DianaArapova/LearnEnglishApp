from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    transcription = models.CharField(max_length=200)
    example = models.CharField(max_length=200)
    sound = models.URLField()

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.URLField()

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=200)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    photo = models.URLField()

    words = models.ManyToManyField(Word)

    def __str__(self):
        return self.name
