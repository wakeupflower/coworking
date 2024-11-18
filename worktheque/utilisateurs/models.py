from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission


class Role(models.TextChoices):
    USER = 'utilisateur', 'Utilisateur'
    ADMIN = 'admin', 'Admin'
    SUPERADMIN = 'superadmin', 'Superadmin'


class CustomUserManager(BaseUserManager):
    def create_user(self, prenom, nom, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(prenom=prenom, nom=nom, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, prenom, nom, email, password=None):
        user = self.create_user(prenom, nom, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# class User(models.Model):
class User(AbstractUser):
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Avoid clashes with auth.User.groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Avoid clashes with auth.User.user_permissions
        blank=True,
    )
    # Informations Personnelles
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # or 'username' if you want to use username
    REQUIRED_FIELDS = ['prenom', 'nom']

    # Personal telephone number
    telephone = models.CharField(max_length=20)

    # Company Information
    entreprise = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    code_postal = models.CharField(max_length=20, null=True, blank=True)

    # Company telephone number
    telephone_entreprise = models.CharField(max_length=20, null=True, blank=True)

    # Company SIREN / SIRET number
    siren_siret = models.CharField(max_length=14, null=True, blank=True)

    # RIB number
    rib_number = models.CharField(max_length=40, null=True, blank=True)

    # Password (hashed in Django)
    password = models.CharField(max_length=255, null=True, blank=True)

    # Date created
    date_created = models.DateTimeField(auto_now_add=True)
    
    abonnement_premium = models.BooleanField(default=False)  # Subscription status

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )

    # Custom related_name to avoid reverse accessor conflicts
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='utilisateur_set',  # Change related_name to avoid clash
    #     blank=True
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='utilisateur_permissions',  # Change related_name to avoid clash
    #     blank=True
    # )
    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.entreprise})"


class Workspace(models.Model):
    # Automatically created primary key field (id) if not specified
    # id = models.AutoField(primary_key=True)  # Only include this if you want to specify the id field explicitly.

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    capacity = models.IntegerField()
    pricePerHour = models.FloatField()
    availability = models.BooleanField()
    
    # Image field to store workspace images
    image = models.ImageField(upload_to='static/workspace_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def check_availability(self):
        return self.availability

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Pending', 'Pending'),
    ]
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'Reservation for {self.workspace} by {self.user}'

    def calculate_price(self):
        duration = (self.endTime.hour - self.startTime.hour) + (self.endTime.minute - self.startTime.minute) / 60
        return duration * self.workspace.pricePerHour

    def cancel_reservation(self):
        self.status = 'Cancelled'
        self.save()

class Payment(models.Model):
    payment_status_choices = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Refunded', 'Refunded'),
    ]
    amount = models.FloatField()
    paymentStatus = models.CharField(max_length=255, choices=payment_status_choices)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return f'Payment for {self.reservation}'

    def process_payment(self):
        self.paymentStatus = 'Completed'
        self.save()

    def refund(self):
        self.paymentStatus = 'Refunded'
        self.save()
