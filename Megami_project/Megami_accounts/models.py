from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserManager(BaseUserManager): 
    def create_user(self, username, email, call_number, password=None):
        if not email:
            raise ValueError('Enter Email!')
        if not call_number:
            raise ValueError('Enter Call Number!')
        user = self.model(
            username = username,
            email = email,
            call_number = call_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.model(
            username = username,
            # email = email,
            # call_number = call_number
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=225, unique = True)
    email = models.EmailField(max_length=225, unique=True)
    call_Number = PhoneNumberField(unique = True, null = False, blank = False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']
    # REQUIRED_FIELDS = ['username','email','call_number']

class Meta:
    db_table = 'user_accounts'

def __str__(self):
    return self.username