from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Room_Type, Apartment
# from .models import Property, Room_Type, Apartment, Reservation
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# from .forms import NewReservationForm
from django.db.models import Count, Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


#View for the Index Page
def index(request):
    # incomplete_reservations()
    my_property = Property.objects.all()[:3]
    return render(request, 'index.html', {'properties':my_property})


def about(request):
    return render(request, 'about.html')

# def properties(request):
#     my_property = Property.objects.all()
#     return render(request, 'properties.html', {'properties':my_property})

class PropertyView(ListView):
    model = Property
    context_object_name = 'properties'
    template_name = 'properties.html'
    paginate_by = 6


def single_property(request, slug):
    myproperty = get_object_or_404(Property, slug=slug)
    room_types = myproperty.room_types.annotate(apartmentCount=Count("apartments", filter=Q(apartments__status__startswith="Avail")))
    fully_booked = True

    # loop through to check if you'll find atleast 1 available apartment, then set a marker
    for i in room_types:
        if i.apartmentCount > 0:
            fully_booked = False
            break

    return render(request, 'single-property.html', {'name':myproperty.name, 'fully_booked':fully_booked, 'description':myproperty.description, 'room_types':room_types})


def available_apartments(request, slug, room_type):
    # myproperty = get_object_or_404(Property, slug=slug)
    room_typee = get_object_or_404(Room_Type, pk=room_type, property__slug=slug)
    available_apartments = Apartment.objects.filter(room_type__pk=room_typee.pk, status__startswith='Avail')
    return render(request, 'available_apartments.html', {'available_apartments':available_apartments, 'room_type':room_typee})

# @login_required
# def reserve_apartment(request, apartment):
#     apartment = get_object_or_404(Apartment, pk=apartment)
#     is_available = apartment.status=="Available"

#    #check if apartment is available. if not, send an error message
#     if not is_available:
#         return render(request, 'reserve_apartment.html', {'apartment': apartment, 'errors':'Sorry! The apartment has been reserved! Kindly try another apartment'})

#     if request.method == 'POST':
#         form = NewReservationForm(request.POST)
#         if form.is_valid():
#             #check if room is available again
#             if is_available:
               
#                 reservation = form.save(commit=False)
#                 reservation.apartment = apartment
#                 reservation.user = request.user
#                 reservation.duration_type = form.cleaned_data.get('duration_type')
#                 reservation.duration = form.cleaned_data.get('duration')
#                 reservation.phone = form.cleaned_data.get('phone')

#                 duration_type = form.cleaned_data.get('duration_type')
#                 duration = form.cleaned_data.get('duration')
#                 price_per_day = apartment.room_type.price_per_day

#                 if duration_type == "Day":
#                     reservation.total_amount = duration * price_per_day
#                 elif duration_type == "Week":
#                     reservation.total_amount = ( duration * 7 ) * price_per_day
#                 elif duration_type == "Month":
#                     reservation.total_amount = ( duration * 30 ) * price_per_day
#                 elif duration_type == "Year":
#                     reservation.total_amount = ( duration * 365 ) * price_per_day

#                 reservation.save()

#                 apartment.status = 'Booked'
#                 apartment.save()


#                 # mail_admins("subject", "message", fail_silently=False, connection=None, html_message=None)
#                 # message = "Hello, " +request.user.get_full_name() + " has made a reservation for "+apartment.name
#                 # send_mail("SummerHill Estates: Apartment Reservation",message, "summer-hill-estates@gmail.com", ['plangepeter@gmail.com', 'frederick.plange@ashesi.edu.gh'], fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)

#                 ##LOOK AT THIS
              
#             else:
#                 return render(request, 'reserve_apartment.html', {'apartment': apartment, 'errors':'Sorry! The apartment has been reserved! Kindly try another apartment'})

#             # return redirect('reservation-success')  
#             return render(request, 'reservation_success.html')      

#     else:
#         form = NewReservationForm()
#     return render(request, 'reserve_apartment.html', {'form':form, 'apartment':apartment})


# def incomplete_reservations():
#     print("Checking incomplete reservations")
#     i_reservervations = Reservation.objects.filter(first_payment__exact="No Payment")
#     current_time = timezone.now()
#     for reservation in i_reservervations:
#         time_diff_hours = (current_time - reservation.date).total_seconds()/3600
#         print(time_diff_hours)
#         # print(dir(reservation.user))
#         # print(reservation.user.get_full_name())
#         # print(reservation.user.email)
#         if time_diff_hours > 24:
#             print("Cancel reservation for {}:".format(reservation.user.get_full_name()))
#             reservation.apartment.status = "Available"
#             reservation.apartment.save()
#             reservation.delete()
#         elif time_diff_hours > 12:
#             print("Send reminder to make payments for {}:".format(reservation.user.get_full_name()))
#             message = "Hello " +reservation.user.get_full_name()+ ", you have made a reservation that you have not paid for. The reservation will be cancelled after 12 hours if no payment is made."
#             send_mail("SummerHill Estates: Apartment Reservation Payment (test)",message, "summer-hill-estates@gmail.com", [reservation.user.email], fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)

# def webhook(request):
