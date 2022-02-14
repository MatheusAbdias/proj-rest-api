from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager para classe usuario"""

    def create_user(self,email,name,password=None):
        """Cria um perfil para um novo usuario"""
        if not email:
            raise ValueError('User most have a email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Cria e salva um nove super usuario"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staf = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Classe que define um usuario em no banco de dados"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #validação feita usando o email
    REQUIRED_FIELDS = ['name'] 

    def get_full_name(self):
        """Retorna o nome completo do usuario"""
        return self.name
    

    def get_short_name(self):
        """retorna primeiro nome"""
        return self.name

    def __str__(self):
        """Representação de um usuario usando o email"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE
    )
    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Representação string do modelo"""
        return self.status_text