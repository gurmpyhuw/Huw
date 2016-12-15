from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime
#from Contact.models import Book
from django import forms
#from Contact import ContactForm
from django.core.mail import send_mail
import Contact

# Create your views here.
#def home(request):
#    return HttpResponse("This will be the home page eventually")

#def hello(request):
#    return HttpResponse("Hello world")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    return render(request, 'current_datetime.html', {'current_date':now})

#def hours_ahead(request, hour_offset):
#    try:
#        hour_offset = int(hour_offset)
#    except ValueError:
#        raise Http404()
#    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
#    return render(request, 'hours_ahead.html', {'next_time':next_time})

#def search_form(request):
#    return render(request, 'search_form.html')

#def search(request):
#    error = False
#    if 'q' in request.GET and request.GET['q']:
#        q = request.GET['q']
#        if q=="":
#            error = True
#        else:
#            books = Book.objects.filter(title__icontains=q)
#            return render(request, 'search_results.html',{'books': books, 'query':q})
#    return render(request, 'search_form.html', {'error':error})

#class ContactForm(forms.Form):
#    subject = forms.CharField()
#    email = forms.EmailField(required=False)
#    message = forms.CharField()

#def contact(request):
#    if request.method == 'POST':
#        form = ContactForm(request.POST)
#        if form.is_valid():
#            cd = form.cleaned_data
#            send_mail(
#                cd['subject'],
#                cd['message'],
#                cd.get('email', 'noreply@example.com'),
#                ['siteowner@example.com'],
#            )
#            return HttpResponseRedirect('/contact/thanks/')
#        else:
#            form = ContactForm()
#        return render(request, 'contact_form.html', {'form':form})
