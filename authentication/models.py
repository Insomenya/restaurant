from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Нужно ввести номер телефона"))
        
        email = self.normalize_email(email)

        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save()
        
        return new_user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Админ должен иметь is_staff = true"))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Админ должен иметь is_superuser = true"))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Админ должен иметь is_active = true"))
        
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username=models.CharField("Имя пользователя", max_length=25, unique=True)
    email=models.CharField("Почта", max_length=80, unique=True)
    phone_number=PhoneNumberField("Номер телефона", null=False, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f"Пользователь {self.username}"