from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm, SignUpForm, EditProfileForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
   return render(request, 'registration/password_success.html', {})



class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')  

    def get_object(self):
        return self.request.user  


