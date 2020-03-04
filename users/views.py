<<<<<<< HEAD
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
=======
>>>>>>> 36c248c88e02e5d5d241a6e74edfdbb51928a90e
