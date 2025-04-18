from django.db import models

class CharacterProfile(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10,blank=True)
    personality=models.TextField()
    backstory=models.TextField(blank=True)
    fear = models.TextField(blank=True)
    dream = models.TextField(blank=True)
    secret = models.TextField(blank=True)

    def __str__(self):
        return self.name
