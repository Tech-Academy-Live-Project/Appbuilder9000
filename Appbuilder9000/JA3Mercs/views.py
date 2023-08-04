from django.shortcuts import render, redirect,  get_object_or_404
from .models import Merc
from .forms import MercForm


# Pathway to Homepage
def ja3_home(request):
    return render(request, 'JA3Mercs/ja3_home.html')

# Pathway to Enroll page
def ja3_enroll(request):
    mercs = Merc.objects.all()
    return render(request, 'JA3Mercs/ja3_enroll.html', {'mercs': mercs})

# Function to
def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Merc, pk=pk)
    form = MercForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('ja3_roster')
        else:
            print(form.errors)
    else:
        return render(request, 'JA3Mercs/ja3_details.html', {'form': form})



def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Merc, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('ja3_roster')
    context = {"item": item,}
    return render(request, "JA3Mercs/ja3_confirmDelete.html", context)

def confirmed(request):
    if request.method == 'POST':
        form = MercForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('ja3_enroll')
    else:
        return redirect('ja3_enroll')

def createRecord(request):
    form = MercForm(request.POST or None)
    form = MercForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ja3_roster')
    else:
        print(form.errors)
        form = MercForm()
    context = { 'form': form }
    return render(request, "JA3Mercs/ja3_createRecord.html", context)

def roster(request):
    mercs = Merc.objects.all
    return render(request, "JA3Mercs/ja3_roster.html", {'mercs': mercs})

