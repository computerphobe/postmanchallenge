from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login.html/",views.login,name="login"),
    path("login.html/distributerdashboard.html/", views.distributor, name="distributor"),
    path("login.html/pharmacydaashboard.html/", views.pharmacy, name="pharmacy"),
    path("login.html/manufacturedashboard.html/", views.manufacture, name="manufacture"),
    path("contact/",views.contact,name="contact"),
    path("getstarted/",views.getStarted,name="getStarted"),
    path("features/", views.features, name="features"),
    path('add/', views.add_drug, name="add_drug"),
    path('track/', views.track_shipment, name="track_shipment"),
    path('mng_inventory_manufacturer/', views.mng_inventory_manufacturer, name="mng_inventory_manufacturer"),
    path('mng_inventory_distributor/', views.mng_inventory_distributor, name="mng_inventory_distributor")
]