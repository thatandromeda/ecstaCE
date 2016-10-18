from django.views.generic.edit import FormView

from .forms import RegistrationForm

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'courses/register.html'
