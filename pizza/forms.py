from django import forms
from django import forms

class PizzaForm(forms.Form):

    topping1 = forms.CharField(label='Topping 1', max_length=27)
    topping2 = forms.CharField(label='Topping 2', max_length=27)
    size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'),('Medium', 'Medium'), ('Large', 'Large')])