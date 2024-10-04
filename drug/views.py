from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import CreateOrder
from .forms import DrugInventoryForm
from django.contrib.auth import authenticate , login
from django.contrib import messages 

import requests

# Create your views here.
def index(request):
    return render(request, "homepage.html")

def login(request):
    return render(request, "login.html")

def distributor(request):
    return render(request, "distributerdashboard.html")

def manufacture(request):
    return render(request, "manufacturedashboard.html")

def pharmacy(request):
    return render(request, "pharmacydaashboard.html")

def contact(request):
    return render(request, "createnewaccount.html")

def getStarted(request):
    return render(request, "login.html")

def features(request):
    return HttpResponse("Features of our application")

def add_drug(request):
    if request.method == 'POST':
        form = DrugInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('distributor')
    else:
        form = DrugInventoryForm()

    return render(request, 'add_drug.html', {'form': form})


def track_shipment(request):
    if request.method == 'POST':
        tracking_no = request.POST.get('tracking_number')
        slug = request.POST.get('slug')
        print(tracking_no)
        print(slug)

        api_url =  f"https://api.aftership.com/tracking/2024-07/trackings/{slug}/{tracking_no}"
        api_key = "asat_2dc7544f0e7c4614836b5fd9dc6c1ab5"

        header = {
            'as-api-key': f'{api_key}',
            'content-type': 'application/json'
        }

        response = requests.get(api_url, headers=header)
        print(response)
        if response.status_code == 200:
            data = response.json()
            tracking_number = data.get('data', {}).get('tracking_number')
            status = data.get('data', {}).get('tag')
            courier_info = data.get('data',{}).get('slug')
            destination_country = data.get('data',{}).get('destination_country_iso3')
            custom_field = data.get('data',{}).get('custom_fields').get('product_name')
            origin_state = data.get('data',{}).get('origin_state')
            print(custom_field)
            print(origin_state)
            print(tracking_number)
            print(courier_info)
            print(status)
            print(destination_country)
            context = {
            'tracking_number': tracking_number,
            'status': status,
            'courier_info':courier_info,
            'destination_country':destination_country,
            'product_name':custom_field,
            'origin_state':origin_state,
        }
            return render(request, 'track_result.html',context)

       
    return render(request, 'track_shipment.html')

def custom_login(request):
        if request.method == 'POST':
         username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page
        else:
            messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html')


def mng_inventory_manufacturer(request):
    return render(request, 'manufacturermanageinventory.html')

def mng_inventory_distributor(request):
    return render(request, "distributermanageinventory.html")
