from asyncio.windows_events import NULL
from django.shortcuts import render
from .forms import PizzaForm

def index(request):
    return render(request, 'index.html')

def order(request):

    if request.method != 'POST':
        form = PizzaForm()
        return render(request, 'order.html', {'pizzaform':form})
    
    note = NULL
    filled_form = PizzaForm(request.POST)
    
    if filled_form.is_valid():
        note = 'Order completed!'
        return render(request, 'order.html', {'pizzaform':filled_form, 'note':note})