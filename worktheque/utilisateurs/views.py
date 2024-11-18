from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import InscriptionForm, ConnexionForm
from .models import User, Workspace, Reservation, Payment
from django.core.files import File
from django.conf import settings
import stripe
import os

# User.objects.all().delete()

# # Create a new User
# user = User.objects.create(name='John Doe', email='john.doe@example.com', password='password', subscriptionStatus=True)

# # Create a new Workspace
# workspace = Workspace.objects.create(name='Co-working Space', type='Shared', capacity=10, pricePerHour=15.0, availability=True)

# # Create a new Reservation
# reservation = Reservation.objects.create(date='2024-11-16', startTime='10:00:00', endTime='12:00:00', status='Confirmed', user=user, workspace=workspace)

# # Create a new Payment for the reservation
# payment = Payment.objects.create(amount=30.0, paymentStatus='Completed', reservation=reservation)


# Vue pour l'inscription
def inscription(request):
    if request.method == 'POST':
        print(request.POST)
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=True)
            user.set_password(form.cleaned_data['password'])
            user = form.save(commit=False)
            user.save()  # Manually save it
        else:
            print(form.errors,"suyantest")  
        # if form.is_valid():
        #     user = form.save()
        #     login(request, user)  # Connecter automatiquement après l'inscription
        #     print("yesyes") 
            # return render(request, "payment/success.html")
            # return redirect('accueil')  # Remplacez 'accueil' par le nom de votre page principale
    else:
        form = InscriptionForm()
    return render(request, './accountcreation.html', {'form': form})



# Vue pour la connexion
def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('accueil')
        else:
            return redirect('accueil')
    else:
        form = ConnexionForm()
    return render(request, './login.html', {'form': form})

def reservationlist(request):
    workspaces = Workspace.objects.all()
    # Pass the workspaces to the template
    return render(request, 'rooms.html', {'workspaces': workspaces})


def workspace_detail(request, id):
    # Retrieve the specific workspace by its ID or return a 404 if not found
    workspace = get_object_or_404(Workspace, id=id)
    # Pass the workspace to the template
    return render(request, 'office.html', {'workspace': workspace})

def cgv(request):
    return render(request, 'cgv.html')  # Render the room page

def myreservation(request):
    return render(request, './myreservations.html') 

def detailreservation(request):
    return render(request, './detailreservation.html') 

def index(request):
    return render(request, 'index.html')  # Render the index page


def create_workspace_with_image(request):
    # Path to the image file
    image_path = os.path.join('media', 'workspace_images', 'image1.jpg')

    # Open the image file
    with open(image_path, 'rb') as f:
        # Create a new Workspace instance
        workspace = Workspace(
            name="New Workspace",
            type="Private Office",
            capacity=10,
            pricePerHour=25.00,
            availability=True,
            image=File(f, name='image1.jpg')  # Set the image field
        )
        # Save the instance to the database
        workspace.save()

    return render(request, 'workspace/success.html')  # Redirect or render a success page


stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_page(request):
    if request.method == "POST":
        try:
            # Crée une session de paiement
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                mode="payment",
                line_items=[
                    {
                        "price_data": {
                            "currency": "eur",
                            "product_data": {
                                "name": "Produit Test",
                            },
                            "unit_amount": 1000,  # Prix en centimes (10 EUR)
                        },
                        "quantity": 1,
                    },
                ],
                success_url=request.build_absolute_uri("/payment/success/"),
                cancel_url=request.build_absolute_uri("/payment/failed/"),
            )
            return render(request, "payment/redirect_to_stripe.html", {"session_id": checkout_session.id})
        except Exception as e:
            return render(request, "payment/error.html", {"error": str(e)})

    return render(request, "payment_page.html", {
        "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY,
    })


def payment_success(request):
    return render(request, "payment/success.html")

def payment_failed(request):
    return render(request, "payment/failed.html")
