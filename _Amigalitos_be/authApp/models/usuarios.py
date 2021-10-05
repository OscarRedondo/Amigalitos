from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.fields import CharField

class UserManager(BaseUserManager):
    def create_user(self, username, usuario_contrasenha=None):
        """"
        Creates and saves a user with the given username and password
        """
        if not username:
            raise ValueError('Users must have an username.')
        user = self.model(username=username)
        user.set_password(usuario_contrasenha)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, usuario_contrasenha):
        """"
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(
            username=username,
            usuario_contrasenha=usuario_contrasenha,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    usuario_id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=15, unique=True)
    usuario_contrasenha = models.CharField('Password', max_length=256)
    usuario_nombre = models.CharField('Name', max_length=30)
    usuario_email = models.EmailField('Email', max_length=100)
    #usuario_dirFacturacion = models.CharField('dirFacturacion', max_length=100)
    #usuario_dirEntrega = models.CharField('Name', max_length=100)
    usuario_ciudad = models.CharField('Name', max_length=30)
    usuario_telefono = models.CharField('Name', max_length=20)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.usuario_contrasenha = make_password(self.usuario_contrasenha, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
