from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import CreateOrder
from .forms import DrugInventoryForm
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

        api_url = "https://api.ship24.com/public/v1/trackers/track"
        api_key = "apik_G76AquuNiNbojGGfM7Hk16hrIxhMod"

        header = {
            'Authorization': f'Bearer {api_key}',
            'content-type': 'application/json'
        }

        payload = {
            "trackingNumber": tracking_no,
        }
        try:
            response = requests.post(api_url, json=payload, headers=header)
            
            if response.status_code == 200:
                # Success - Parse and display the data
                data = response.json()
                context = {'shipment_data': data, 'tracking_number': tracking_no}
                return render(request, 'track_result.html', context)
            else:
                # Handle API errors like 404, 500, etc.
                error_message = f"Failed to fetch data from Ship24 API. Status code: {response.status_code}"
                return render(request, 'track_result.html', {'error': error_message})

        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'track_result.html', {'error': error_message})

       
    return render(request, 'track_shipment.html')
