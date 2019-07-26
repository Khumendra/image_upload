from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from .models import Hotel

# Create your own views here.
def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html',{'form':form})

def sucess(request):
    return HttpResponse('successfully uploaded')

# Python program to view
# for displaying images

def display_hotel_images(request):
    if request.method == 'GET':
        Hotels = Hotel.objects.all()
        return render(request,'display_hotel_images.html',{'hotel_images':Hotels})
