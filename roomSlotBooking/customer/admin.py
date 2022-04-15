from django.contrib import admin
from .models import Customers, booking, manager, records, room, rules

# Register your models here.

admin.site.register(Customers)
admin.site.register(manager)
admin.site.register(room)
admin.site.register(rules)
admin.site.register(booking)
admin.site.register(records)