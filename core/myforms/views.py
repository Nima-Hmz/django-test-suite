from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from myforms.forms.first_form import NameForm

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
    

        
