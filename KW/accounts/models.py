from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager
from multiselectfield import MultiSelectField
from django.db import models


Key_Press = [
    (1, "가벼움"),
    (2, "무거움"),
    (3, "상관없음"),
]
Array = [
    (1, "풀배열"),
    (2, "텐키리스"),
    (3, "상관없음"),
]
Sound = [
    (1, "경쾌한 소리"),
    (2, "조용한 소리"),
    (3, "상관없음"),
]
Weight = [
    (1, "가벼움"),
    (2, "상관없음"),
]
connect = [
    (1, "유선"),
    (2, "무선"),
    (3, "상관없음"),
]



class UserManager(BaseUserManager):
    def create_user(self, email, password, nickname, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user



class User(AbstractUser):
    press = MultiSelectField(choices=Key_Press, null=True)
    weight = MultiSelectField(choices=Weight, null=True)
    array = MultiSelectField(choices=Array, null=True)
    sound = MultiSelectField(choices=Sound, null=True)
    connect = MultiSelectField(choices=connect, null=True)
    pass
