from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Commander(models.Model):
    name = models.CharField(max_length=50, verbose_name="Commander name")
    year = models.IntegerField(verbose_name="Commander year")
    did = models.CharField(max_length=255, verbose_name="Commander did")
    area = models.CharField(max_length=255, verbose_name="Commander area")
    image = models.ImageField(upload_to="commander/")
    commander_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Commander list"
        db_table = "commander"
