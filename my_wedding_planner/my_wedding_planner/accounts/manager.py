from django.contrib.auth.base_user import BaseUserManager


class WeddingPlannerManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')

        return self._create_user(email, password, **extra_fields)

    # def _create_user(self, email, password, **extra_fields):
    #     if not email:
    #         raise ValueError('The given email must be set')
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_user(self, email, password=None):
    #     """
    #     Creates a user with the given username, email and password.
    #     """
    #     if not email:
    #         raise ValueError("Users must provide an email address.")
    #     # if not username:
    #     #     raise ValueError("Users must have a username.")
    #
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         # username=username,
    #     )
    #
    #     user.set_password(password)
    #     user.is_active = True
    #     user.save(using=self._db)
    #     return user
    #
    # def create_superuser(self, email, password=None):
    #     user = self.create_user(email=email, password=password)
    #
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.is_active = True
    #     user.save(using=self._db)
    #     return user
