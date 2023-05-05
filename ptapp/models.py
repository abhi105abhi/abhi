from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    class_level = models.CharField(max_length=20)
    subjects = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    class_level = models.CharField(max_length=20)
    subjects = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
