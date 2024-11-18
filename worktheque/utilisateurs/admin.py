from django.contrib import admin
from .models import User, Workspace, Reservation, Payment

admin.site.register(User)
admin.site.register(Workspace)
admin.site.register(Reservation)
admin.site.register(Payment)

