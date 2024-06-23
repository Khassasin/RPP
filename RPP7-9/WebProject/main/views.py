from django.shortcuts import render, redirect
from .models import *
from .forms import CustomersForm


def index(request, table=Customers):
    fields_name = [f.name for f in table._meta.fields]
    table_name = table.__name__
    query_results = table.objects.all()
    return render(request, 'main/index.html', locals())


def edit(request, id):
    instance = Customers.objects.get(id=id)
    if request.method == 'POST':
        form = CustomersForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomersForm(instance=instance)
    context = {'form': form}
    return render(request, 'main/edit.html', context)


def add_new(request):
    if request.method == 'POST':
        form = CustomersForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomersForm()
    context = {'form': form}
    return render(request, 'main/edit.html', context)


def remove(request, id):
    if request.method == 'POST':
        instance = Customers.objects.get(id=id)
        instance.delete()
        return redirect('/')


def change_table(request):
    if 'Customers' in request.POST:
        return index(request, Customers)
    elif "Calls" in request.POST:
        return index(request, Calls)
    elif "Call_Reasons" in request.POST:
        return index(request, Call_Reasons)
    elif "Reasons" in request.POST:
        return index(request, Reasons)
    else:
        return index(request, Resolutions)