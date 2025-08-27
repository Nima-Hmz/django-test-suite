from typing import Any
from django import forms

class TicketForm(forms.Form):
    template_name = 'myforms/forms/second.html'

    sender = forms.CharField(max_length=128, label='ارسال کننده', widget=forms.TextInput(attrs={'x':'y'}))
    message = forms.CharField(widget=forms.Textarea, label='پیام')
    receiver = forms.CharField(max_length=128, label='دریافت گننده')
    rate = forms.IntegerField(label='امتیاز')

    def clean_sender(self):
        sender = self.cleaned_data.get('sender', '').strip()

        if sender == 'nima':
            raise forms.ValidationError('شما نمیتوانید اسم نیما را وارد کنید')
        
        return sender
    

    def clean(self):
        cleaned_data = super().clean()

        sender = cleaned_data.get('sender', '').strip()
        message = cleaned_data.get('message', '').strip()

        if sender == message:
            raise forms.ValidationError("مثه آدم تیکت بده")
        
        return cleaned_data
