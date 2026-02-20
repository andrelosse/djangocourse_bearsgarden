from django import forms
from .models import BakeryItem, Category

class BakeryItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = BakeryItem
        fields = ['name', 'description', 'price', 'category']
        labels = {
            'name': 'Item Name: ',
            'description': 'Description: ',
            'price': 'Price: ',
            'category': 'Category: '}

class MultipleItems(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=5)