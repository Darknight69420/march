from django.contrib import admin
from .models import Employee
from .models import Regional_Service
from .models import Staff_Position

admin.site.register(Employee)
admin.site.register(Staff_Position)
admin.site.register(Regional_Service)

