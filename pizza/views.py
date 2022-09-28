from asyncio.windows_events import NULL
from textwrap import fill
from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzas
from django.forms import formset_factory

def index(request):
    return render(request, 'index.html')

def order(request):

    multiple_form = MultiplePizzas()

    if request.method != 'POST':
        form = PizzaForm()
        return render(request, 'order.html', {'pizzaform':form, 'multiple_form':multiple_form})
    
    note = NULL
    filled_form = PizzaForm(request.POST)
    
    if filled_form.is_valid():
        note = 'Order completed!'
        return render(request, 'order.html', {'pizzaform':filled_form, 'note':note, 'multiple_form':multiple_form})

def pizzas(request):
    number_pizzas = 2

    filled_number = MultiplePizzas(request.GET)
    if filled_number.is_valid():
        number_pizzas = filled_number.cleaned_data['number']
    
    PizzaFormSet = formset_factory(PizzaForm, extra=number_pizzas)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)

        if filled_formset.is_valid():
            note = 'Order completed!!'
        else:
            note = 'Order failed, check your pizzas and try again!'

        return render(request, 'pizzas.html', {'note':note, 'formset':formset})
    
    else:
        return render(request, 'pizzas.html', {'formset':formset})