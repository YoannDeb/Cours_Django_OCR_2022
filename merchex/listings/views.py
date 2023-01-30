from django.shortcuts import render
from django.http import HttpResponse
from .models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    context = {
        'bands': bands,
    }
    return render(request, 'listings/band_list.html', context)

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    context = {
        'band': band,
    }
    return render(request, 'listings/band_detail.html', context)

def listings(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'listings/listings.html', context)

def about_us(request):
    return render(request, 'listings/about-us.html')


def contact(request):
    return render(request, 'listings/contact.html')