from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    result_general = models.IntegerField(verbose_name='Общие вопросы', default=0)
    result_safe = models.IntegerField(verbose_name='Безопасные методы', default=0)
    result_danger = models.IntegerField(verbose_name='Повышенная опасность', default=0)
    result_personal = models.IntegerField(verbose_name='Индивидуальная защита', default=0)
    result_aid = models.IntegerField(verbose_name='Первая помощь', default=0)

    read_general = models.IntegerField(verbose_name='R_Общие вопросы', default=0)
    read_safe = models.IntegerField(verbose_name='R_Безопасные методы', default=0)
    read_danger = models.IntegerField(verbose_name='R_Повышенная опасность', default=0)
    read_personal = models.IntegerField(verbose_name='R_Индивидуальная защита', default=0)
    read_aid = models.IntegerField(verbose_name='R_Первая помощь', default=0)

    max_general = models.IntegerField(verbose_name='Max_Общие вопросы', default=27)
    max_safe = models.IntegerField(verbose_name='Max_Безопасные методы', default=23)
    max_danger = models.IntegerField(verbose_name='Max_Повышенная опасность', default=9)
    max_personal = models.IntegerField(verbose_name='Max_Индивидуальная защита', default=27)
    max_aid = models.IntegerField(verbose_name='Max_Первая помощь', default=27)

    result_score = models.IntegerField(verbose_name='Общая оценка', default=0)
