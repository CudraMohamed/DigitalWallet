from django.contrib import admin
from .models import Customer
# admin.site.register (Customer)


# Register your models here.
# add model amin
#Access Admin dashboard

#Add a model to the admin panel
# class CustomerAdmin(admin.ModelAdmin):
#     list_display=('first_name','last_name','age','email')
#     search_details=('first_name','last_name')

admin.site.register(Customer)