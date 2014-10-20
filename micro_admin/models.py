from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


GENDER_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

USER_ROLES = (
        ('BranchManager','BranchManager'),
        ('LoanOfficer', 'LoanOfficer'),
        ('Cashier', 'Cashier')
    )

ACCOUNT_TYPES = (
        ('SavingsAccount', 'SavingsAccount'),
        ('LoanAccount', 'LoanAccount')
    )

CLIENT_ROLES = (
        ('FirstLeader','FirstLeader'),
        ('SecondLeader', 'SecondLeader'),
        ('GroupMember', 'GroupMember')
    )

class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    opening_date = models.DateField()
    #location = models.TextField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    pincode = models.IntegerField()


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Users must have an username')

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):

        user = self.create_user(username, password=password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField( max_length=255, unique=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(choices = GENDER_TYPES ,max_length = 10)
    branch = models.ForeignKey(Branch)
    user_roles = models.CharField(choices= USER_ROLES, max_length=20)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    mobile = models.BigIntegerField()
    pincode = models.BigIntegerField()

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username


class Clients(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True, null=True)
    account_type = models.CharField(choices=ACCOUNT_TYPES, max_length=20)
    account_number = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10,null=True)
    gender = models.CharField(choices = GENDER_TYPES ,max_length=10)
    clent_role = models.CharField(choices=CLIENT_ROLES, max_length=20)
    occupation = models.CharField(max_length=200)
    annual_income = models.BigIntegerField()
    joined_date = models.DateField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20,default=True,null=True)
    pincode = models.CharField(max_length=20,default=True,null=True)
    photo = models.ImageField(upload_to=settings.PHOTO_PATH,null=True)
    signature = models.ImageField(upload_to =settings.SIGNATURE_PATH,null=True)
    is_active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch)


class Groups(models.Model):
    name = models.CharField(max_length=200, unique=True)
    account_type = models.CharField(choices=ACCOUNT_TYPES, max_length=20)
    account_number = models.CharField(max_length=50, unique=True)
    activation_date = models.DateField()
    is_active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch)
    clients = models.ManyToManyField(Clients)


class Centers(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_date = models.DateField()
    is_active = models.BooleanField(default=True)
    branch = models.ForeignKey(Branch)
    groups = models.ManyToManyField(Groups)
