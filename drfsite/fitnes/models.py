from django.db import models


class Session(models.Model):
    title = models.CharField(max_length=255)
    session = models.ForeignKey('CatSession', on_delete=models.PROTECT, null=True)
    direction = models.ForeignKey('CatDirection', on_delete=models.PROTECT, null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    coach = models.ForeignKey('CatCoach', on_delete=models.PROTECT, null=True)
    detail_info = models.TextField(max_length=5000)

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятие'

    def __str__(self):
        return self.title


class CatSession(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name = 'Категория Занятие'
        verbose_name_plural = 'Категория Занятие'

    def __str__(self):
        return self.name


class CatDirection(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name = 'Категория Направление'
        verbose_name_plural = 'Категория Направление'

    def __str__(self):
        return self.name


class CatCoach(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name = 'Категория Тренер'
        verbose_name_plural = 'Категория Тренер'

    def __str__(self):
        return self.name
