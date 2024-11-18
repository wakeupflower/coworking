from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for the index page
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('cgv/', views.cgv, name='cgv'),
    path('reservationlist/', views.reservationlist, name='reservationlist'),
    path('workspace/<int:id>/', views.workspace_detail, name='workspace_detail'),  
    path('myreservation/', views.myreservation, name='myreservation'),
    path('detailreservation/', views.detailreservation, name='detailreservation'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
    path("payment/", views.payment_page, name="payment_page"),
    path("payment/success/", views.payment_success, name="payment_success"),
    path("payment/failed/", views.payment_failed, name="payment_failed"),
]

 # Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)