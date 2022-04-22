from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    username = models.CharField(max_length=16)
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
        error_messages={'unique': "Такой пользователь уже есть"},
    )

    def __str__(self):
        return str(self.email)[:15]


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(
        verbose_name="День рождения", blank=True, default='1111-11-11'
    )

    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительные поля'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
