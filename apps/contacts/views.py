from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        #send mail
        send_mail(
            'Interior Design Inquiry',
            'There has been an inquiry Sign in to admin for more info',
            'info@interiorsafi.co.ke',
            [email],
            fail_silently=False
        )

        messages.success(request, 'Thank You. Your request has been submitted, we will get back to you ASAP.')
        return redirect('/contacts/')
    else:
        return render(request, 'contacts/contacts.html')
