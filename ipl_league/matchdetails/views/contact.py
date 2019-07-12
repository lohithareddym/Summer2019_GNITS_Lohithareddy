from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from forms.forms import ContactForm

class emailView(View):
    def get(self,request):
        form = ContactForm()
        return render(request, "contactform.html", {'form': form})
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
        return render(request, "contactform.html", {'form': form})

class successView(View):
    def get(self,request):
        return HttpResponse('Success! Thank you for your message.')