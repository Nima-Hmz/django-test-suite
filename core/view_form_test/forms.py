from django import forms


class ProductForm(forms.Form):
    template_name = 'third/forms/product_form.html'

    name = forms.CharField(max_length=124, label="نام")
    price = forms.IntegerField(label='قیمت')
    stock_count = forms.IntegerField(max_value=99, label="تعداد")

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise forms.ValidationError("قیمت نمیتواند منفی باشد")
        
        return price 
    
    def clean_stock_count(self):
        stock_count = self.cleaned_data.get('stock_count')

        if stock_count < 0:
            raise forms.ValidationError("تعداد نمیتواند کمتر از صفر باشد")
        
        return stock_count
    
    def clean(self):
        cleaned_data = super().clean()
        price = price = self.cleaned_data.get('price')
        stock_count = self.cleaned_data.get('stock_count')


        if price == stock_count:
            raise forms.ValidationError('قیمت با تعداد نمیتواند یکی باشد')
        
        return cleaned_data