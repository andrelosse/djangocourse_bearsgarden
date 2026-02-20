from django.shortcuts import render, redirect
from .forms import BakeryItemForm, MultipleItems
from django.forms import formset_factory
from .models import BakeryItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def order(request):
    multiple_form = MultipleItems()

    if request.method != 'POST':
        form = BakeryItemForm()
        return render(request, 'order.html', {'itemform':form, 'multiple_form':multiple_form})
    
    filled_form = BakeryItemForm(request.POST)
    
    if filled_form.is_valid():
        created_item = filled_form.save(commit=False)
        created_item.user = request.user
        created_item.save()
        created_item_pk = created_item.id
        note = 'Order completed!'
        return render(request, 'order.html', {
            'itemform':filled_form, 
            'note':note, 
            'multiple_form':multiple_form, 
            'created_item_pk':created_item_pk })

@login_required
def order_multiple(request):
    number_items = 2

    filled_number = MultipleItems(request.GET)
    if filled_number.is_valid():
        number_items = filled_number.cleaned_data['number']
    
    BakeryItemFormSet = formset_factory(BakeryItemForm, extra=number_items)
    formset = BakeryItemFormSet()

    if request.method == 'POST':
        filled_formset = BakeryItemFormSet(request.POST)

        if filled_formset.is_valid():
            for form in filled_formset:
                if form.cleaned_data:
                    item = form.save(commit=False)
                    item.user = request.user
                    item.save()
            note = 'Order completed!!'
        else:
            note = 'Order failed, check your items and try again!'

        return render(request, 'order_multiple.html', {'note':note, 'formset':filled_formset})
    
    else:
        return render(request, 'order_multiple.html', {'formset':formset})

@login_required
def edit_order(request, pk):
    note = ''
    item = BakeryItem.objects.get(pk=pk, user=request.user)
    form = BakeryItemForm(instance=item)

    if request.method == 'POST':
        filled_form = BakeryItemForm(request.POST, instance=item)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order updated!'

    return render(request, 'edit_order.html', {'itemform':form, 'item':item, 'note':note})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def order_history(request):
    items = BakeryItem.objects.filter(user=request.user)
    return render(request, 'history.html', {'items': items})