from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render,redirect
from matchdetails.forms import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if(self.request.path==reverse('login')):
            input_form = forms.LoginForm()
            title='login'
        else:
            input_form=forms.SignUpForm()
            title='signup'
        return render(request, template_name='login.html',context={'form':input_form})

    def post(self, request, *args, **kwargs):
         input_form = forms.LoginForm(request.POST)
         signup_form=forms.SignUpForm(request.POST)
         if self.request.path == reverse('login'):
             # print('entered user login')
             if (input_form.is_valid()):
                 user = authenticate(request, username=input_form.cleaned_data['username'],
                                     password=input_form.cleaned_data['password'])
             if user is not None:
                 login(request, user)
                 return HttpResponseRedirect('/seasons/')
             else:
                 messages.error(request, 'invalid credentials')
         if self.request.path==reverse('signin'):
             if(signup_form.is_valid()):
                 user = User.objects.create_user(username=signup_form.cleaned_data["username"],email=signup_form.cleaned_data["email"],password=signup_form.cleaned_data["password"])
                 user.save()
         return HttpResponseRedirect('/login_error/')
class loginwithmessage(View):
    def login_with_msg(self,request):
        input_form = forms.LoginForm()
        return render(request, template_name='login_error.html', context={'form': input_form})