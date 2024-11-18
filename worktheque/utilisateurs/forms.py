from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator, EmailValidator
from .models import User


    

# Formulaire de connexion (personnalisé si nécessaire)
class ConnexionForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


# Formulaire d'inscription
class InscriptionForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['prenom', 'nom', 'email', 'password', 'confirm_password']


        # fields = ['prenom', 'email', 'password']
        # fields = ['prenom', 'nom', 'telephone', 'abonnement_premium', 'email', 'entreprise', 'telephone_entreprise', 'adresse', 'ville', 'code_postal', 'siren_siret', 'rib_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # if password != confirm_password:
        #     raise forms.ValidationError(password,confirm_password)
        return cleaned_data
    

    # # Personal Information
    # prenom = forms.CharField(
    #     label="Prénom",
    #     max_length=50,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre prénom'}),
    #     required=True
    # )
    # nom = forms.CharField(
    #     label="Nom",
    #     max_length=50,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
    #     required=True
    # )
    # email = forms.EmailField(
    #     label="Adresse e-mail",
    #     validators=[EmailValidator()],
    #     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre e-mail'}),
    #     required=True
    # )
    # telephone_personnel = forms.CharField(
    #     label="Numéro de téléphone personnel",
    #     max_length=15,
    #     validators=[
    #         RegexValidator(
    #             regex=r'^\+?\d{9,15}$',
    #             message="Veuillez entrer un numéro de téléphone valide (jusqu'à 15 chiffres)."
    #         )
    #     ],
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: +33123456789'}),
    #     required=True
    # )

    # # Company Information
    # entreprise = forms.CharField(
    #     label="Nom de l'entreprise",
    #     max_length=100,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'entreprise"}),
    #     required=False
    # )
    # adresse = forms.CharField(
    #     label="Adresse",
    #     max_length=200,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complète'}),
    #     required=True
    # )
    # ville = forms.CharField(
    #     label="Ville",
    #     max_length=50,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
    #     required=True
    # )
    # code_postal = forms.CharField(
    #     label="Code Postal",
    #     max_length=10,
    #     validators=[
    #         RegexValidator(
    #             regex=r'^\d{4,10}$',
    #             message="Veuillez entrer un code postal valide."
    #         )
    #     ],
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code postal'}),
    #     required=True
    # )
    # telephone_entreprise = forms.CharField(
    #     label="Numéro de téléphone de l'entreprise",
    #     max_length=15,
    #     validators=[
    #         RegexValidator(
    #             regex=r'^\+?\d{9,15}$',
    #             message="Veuillez entrer un numéro de téléphone valide (jusqu'à 15 chiffres)."
    #         )
    #     ],
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: +33123456789'}),
    #     required=False
    # )
    # siren_siret = forms.CharField(
    #     label="SIREN / SIRET",
    #     max_length=14,
    #     validators=[
    #         RegexValidator(
    #             regex=r'^\d{9}|\d{14}$',
    #             message="Le SIREN doit contenir 9 chiffres et le SIRET doit contenir 14 chiffres."
    #         )
    #     ],
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 123456789 ou 12345678912345'}),
    #     required=False
    # )
    # rib = forms.CharField(
    #     label="Numéro RIB",
    #     max_length=23,
    #     validators=[
    #         RegexValidator(
    #             regex=r'^[A-Z0-9]{14,23}$',
    #             message="Veuillez entrer un numéro RIB valide (entre 14 et 23 caractères alphanumériques)."
    #         )
    #     ],
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro RIB'}),
    #     required=False
    # )

    # # Password
    # password = forms.CharField(
    #     label="Mot de passe",
    #     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
    #     min_length=8,
    #     required=True
    # )
    # confirm_password = forms.CharField(
    #     label="Confirmer le mot de passe",
    #     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}),
    #     required=True
    # )

    # # General Conditions
    # conditions = forms.BooleanField(
    #     label="J'accepte les Conditions Générales",
    #     required=True
    # )
    #     # class Meta:
    #     #     model = User
    #     #     fields = ['username', 'email', 'password1', 'password2']

    # def clean(self):
    #     """
    #     Custom validation for password confirmation.
    #     """
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password and confirm_password and password != confirm_password:
    #         raise forms.ValidationError("Les mots de passe ne correspondent pas.")

    #     return cleaned_data
