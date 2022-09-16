from django.contrib import admin
from TinyCoder.models import Contact
from TinyCoder.models import SIGNUP
from TinyCoder.models import LOGIN
from TinyCoder.models import APPOINTMENT

# Register your models here.
admin.site.register(Contact)
admin.site.register(SIGNUP)
admin.site.register(LOGIN)
admin.site.register(APPOINTMENT)