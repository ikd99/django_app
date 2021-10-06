from django.contrib import admin

# Register your models here.
from django.contrib import admin
from main.models import user_info, request, message, payment, favorite

admin.site.register(user_info)
admin.site.register(request)
admin.site.register(message)
admin.site.register(payment)
admin.site.register(favorite)