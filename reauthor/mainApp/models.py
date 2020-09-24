from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isAuthor = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user

#등록된 작품 정보
class Toon(models.Model):
    userID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    genre = (models.CharField(max_length=30))
    url = models.TextField()
    detail = models.TextField()
    thumbnail = models.ImageField(upload_to='images/')

#회차 정보
class Restory(models.Model):
    toonID = models.ForeignKey(Toon, on_delete=models.CASCADE)
    chapterNum = models.IntegerField()
    detail = models.TextField()
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(default=timezone.now)

#작품 속 등장인물
class Characters(models.Model):
    toonID = models.ForeignKey(Toon, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    detail = models.TextField()

#회차별 등장인물 위치 값
class CharactersPosition(models.Model):
    toonID = models.ForeignKey(Toon, on_delete=models.CASCADE)
    chapterID = models.ForeignKey(Restory, on_delete=models.CASCADE, related_name="restory")
    posX = models.FloatField()
    posY = models.FloatField()
