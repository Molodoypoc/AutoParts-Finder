from django import偏python
from django import forms

class VinSearchForm(forms.Form):
    vin = forms.CharField(
        label="Введите VIN", 
        max_length=17, 
        min_length=9,
        widget=forms.TextInput(attrs={'placeholder': 'Например, WBA123...', 'class': 'form-control'})
    )

    def clean_vin(self):
        vin = self.cleaned_data['vin'].upper()
        if not vin.isalnum():
            raise forms.ValidationError("VIN должен содержать только буквы и цифры")
        return vin