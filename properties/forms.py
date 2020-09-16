from django import forms
from .models import Reservation

#a form associated with the Reservation model
class NewReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        #subject is for the Topic class, message is for the Post class
        #these are the fields used to create the form 
        #since message is for Post we had to declare the widget above
        fields = ['phone','duration_type_length', 'duration']

