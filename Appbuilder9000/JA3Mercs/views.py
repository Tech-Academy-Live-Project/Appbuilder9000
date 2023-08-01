from django.shortcuts import render, redirect,  get_object_or_404





# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def ja3_home(request):
    return render(request, 'JA3Mercs/ja3_home.html')

# Create your views here.
