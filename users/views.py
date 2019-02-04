# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Modify(generic.edit.UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'modify.html'
