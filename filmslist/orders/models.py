from django.db import models
from django.utils import timezone


class Translators(models.Model):       #класс для бд с работниками
    user_name = models.CharField(max_length=20, default="Karen")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True, help_text="Enter your e-mail")
    phone = models.IntegerField(null=True, blank=True, help_text="Enter your phone number")
    languages = models.CharField(max_length=20, null=True, blank=True, help_text="Enter your working languages")
    admission = models.ForeignKey('TranslationTypes', help_text="Enter your types of admission", on_delete=models.SET_NULL, null=True, blank=True,)

    def __str__(self):
        return self.user_name


class TranslationTypes(models.Model):      #класс для типа перевода
    type = models.CharField(max_length=20, help_text="subtitles, voiceover, dubbing")

    def __str__(self):
        return self.type


class MovieType(models.Model):      #класс для типа контента
    type = models.CharField(max_length=20, help_text="Film or serial")

    def __str__(self):
        return self.type


class LanguagePairs(models.Model):    #класс для языковых пар
    name = models.CharField(max_length=200, help_text="ru-en, en-ru, de-en etc.")

    def __str__(self):
        return self.name


class Order(models.Model):     #класс для выполненных заказов
    language = models.ForeignKey('LanguagePairs', on_delete=models.SET_NULL, null=True, blank=True, help_text="ru-en, en-ru, de-en etc.")
    translation_type = models.ForeignKey('TranslationTypes', on_delete=models.SET_NULL, null=True, blank=True)
    movie_type = models.ForeignKey('MovieType', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True, help_text="name of movie.")
    episode = models.IntegerField(null=True, blank=True,)
    duration = models.IntegerField(null=True, blank=True,)
    rate = models.IntegerField(null=True, blank=True,)
    receipt_date = models.DateField(null=True, blank=True,)
    deadline = models.DateField(null=True, blank=True,)
    translator = models.ForeignKey('Translators', on_delete=models.SET_NULL, null=True, blank=True)
    ORDER_STATUS = (
    ('w', 'on progress'),
    ('d', 'delivered'),
    )
    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='w')

    def __str__(self):
        return self.title

    def get_price(self):
        return self.duration * self.rate


class Post(models.Model):   #класс для постов о новой работе
    title = models.CharField(max_length=50, null=True, blank=True, help_text="name of movie.")
    date_posted = models.DateTimeField(default=timezone.now)
    language = models.ForeignKey('LanguagePairs', on_delete=models.SET_NULL, null=True, blank=True,
                                 help_text="ru-en, en-ru, de-en etc.")
    translation_type = models.ForeignKey('TranslationTypes', on_delete=models.SET_NULL, null=True, blank=True)
    movie_type = models.ForeignKey('MovieType', on_delete=models.SET_NULL, null=True, blank=True)
    episode = models.IntegerField(null=True, blank=True, )
    duration = models.IntegerField(null=True, blank=True, )
    rate = models.IntegerField(null=True, blank=True, )
    deadline = models.DateField(null=True, blank=True, )

    def __str__(self):
        return self.title
