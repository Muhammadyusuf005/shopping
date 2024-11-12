from django.contrib import admin
from django.contrib.auth.models import User

from apps.general.models import General, PaymentMethod


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    pass

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass
