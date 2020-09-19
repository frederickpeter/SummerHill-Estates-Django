from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#variables for the admin dashboard
admin.site.site_header = 'Summer Hill Estates Administration'
admin.site.site_title = 'Summer Hill Estates Admin'

# Unregister the provided model admin
admin.site.unregister(User)

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    search_fields = ("name__contains", )
    list_per_page = 10
# admin.site.register(Facility)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    search_fields = ("name__contains", )
    list_per_page = 10
    prepopulated_fields = {"slug": ("name",)}
# admin.site.register(Property)

@admin.register(Room_Type)
class Room_Type_Admin(admin.ModelAdmin):
    search_fields = ("capacity__contains", )
    list_per_page = 10
# admin.site.register(Room_Type)

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("room_type", "name")
    search_fields = ("name__icontains", "room_type__property__name__icontains")
    list_per_page = 10
#admin.site.register(Room)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    search_fields = ("user__first_name__icontains", "user__last_name__icontains", "apartment__name__icontains", "phone__contains")
    list_per_page = 10
#admin.site.register(Reservation)

@admin.register(Property_Facility)
class Property_FacilityAdmin(admin.ModelAdmin):
    search_fields = ("property__name__icontains", "facility__name__icontains")
    list_per_page = 10
#admin.site.register(Property_Facility)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    # search_fields = ("property__name__icontains", "facility__name__icontains")
    list_per_page = 10
#admin.site.register(Property_Facility)


# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #prevent all users from being able to update the date joined and last_login field
    readonly_fields = [
        'date_joined', 'last_login', 'password'
    ]
    #controls what is displayed in the table
    list_display = ("username", "first_name", "last_name", "email", "is_staff")
    list_per_page = 10

    #prevent staff from updating the username of a user
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'is_staff',
                'user_permissions',
                'email',
                'is_active' 
                
            }


        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
            if f == 'email' and obj == request.user:
                form.base_fields[f].disabled=False
            if obj != None:
                if f == 'is_active' and  obj.is_superuser == False and obj.is_staff==False:
                    form.base_fields[f].disabled=False
                elif f == 'username' and  obj.is_superuser == False and obj.is_staff==False:
                    form.base_fields[f].disabled=False
            else:
                form.base_fields['username'].disabled=False

        return form