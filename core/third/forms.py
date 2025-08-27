from django import forms

class ProductForm(forms.Form):
    template_name = 'third/forms/product_form.html'

    name = forms.CharField(max_length=100, label='نام')
    price = forms.DecimalField(label='قیمت')
    stock_count = forms.IntegerField(label='موجودی')

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise forms.ValidationError("قیمت نمیتواند منفی باشد")
        
        return price
    
    def clean_stock_count(self):
        stock_count = self.cleaned_data.get('stock_count')

        if stock_count < 0:
            raise forms.ValidationError("تعداد نمیتواند کمتر از صفر باشد")
        
        return self.cleaned_data