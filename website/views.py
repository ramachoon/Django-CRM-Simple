from django.shortcuts import render,reverse,get_object_or_404
from website.models import Record
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from website.forms import RecordForm



def home(request):
    records = Record.objects.all()
    context = {"records":records}
    return render(request, 'home.html', context)




def customer_record(request, pk):
    customer_record = Record.objects.get(id=pk)
    context = {"customer_record":customer_record}
    return render(request, 'record.html', context)




def delete_record(request, pk):
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Deleted")
    return HttpResponseRedirect(reverse('website:home'))


def add_record(request):
    form = RecordForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return HttpResponseRedirect(reverse("website:home"))
    messages.success(request, 'create succesfully')
    context = {"form":form}
    return render(request, 'add_record.html', context)


def update_record(request, pk):
    current_record = Record.objects.get(id=pk)
    form = RecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Update")
        return HttpResponseRedirect(reverse("website:home"))
    return render(request, 'update_record.html', {'form':form})