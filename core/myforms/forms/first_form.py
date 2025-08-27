from django import forms

class NameForm(forms.Form):
    template_name = 'myforms/forms/form_snippet.html'
    name = forms.CharField(max_length=100, label='your name')

