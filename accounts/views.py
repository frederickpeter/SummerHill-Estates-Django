from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView
from django.contrib.auth.decorators import login_required
from properties.models import Reservation


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('accounts:my_account')

    def get_object(self):
        return self.request.user


def my_dashboard(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'accounts/my_dashboard.html', {'reservations':reservations})

@method_decorator(login_required, name='dispatch')
class DashboardView(ListView):
    model = Reservation
    context_object_name = 'reservations'
    template_name = 'accounts/my_dashboard.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Reservation.objects.filter(user=self.request.user)
        return queryset


@login_required
def cancel_reservation(request, reservation):
    reservation = get_object_or_404(Reservation, pk=reservation, user=request.user)
    reservation.delete()
    return redirect('accounts:my_dashboard') 


