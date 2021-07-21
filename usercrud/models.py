from django.db import models


class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 15)

    def __str___(self):
        return self.name