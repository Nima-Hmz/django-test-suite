from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from myforms.forms.first_form import NameForm
from myforms.forms.second_form import TicketForm

# Create your views here.

class FirstView(View):
    def get(self, request):
        name_form = NameForm()
        context = {
            'name_form':name_form
        }
        return render(request, 'myforms/first.html', context)
    

    def post(self, request):
        name_form = NameForm(request.POST)

        if name_form.is_valid():
            name_form_data = name_form.cleaned_data
            return redirect('myforms:first')
        
        return HttpResponse("data is not valid")
    

class SecondView(View):
    def get(self, request):
        ticket_form = TicketForm()
        context = {
            'ticket_form':ticket_form
        }
        return render(request, 'myforms/second_template.html', context)
    
    def post(self, request):
        ticket_form = TicketForm(request.POST)

        if ticket_form.is_valid():
            sender = ticket_form.cleaned_data.get('sender', '').strip()
            return HttpResponse(f'your form was ok, this is your {sender}')
        
        context = {
            'ticket_form':ticket_form
        }
        return render(request, 'myforms/second_template.html', context)

        
