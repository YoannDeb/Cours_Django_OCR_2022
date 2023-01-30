from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    context = {
        'bands': bands,
    }
    return render(request, 'listings/band_list.html', context)

def band_detail(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    context = {
        'band': band,
    }
    return render(request, 'listings/band_detail.html', context)

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'listings/listing_list.html', context)

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing_detail.html', context)
def about_us(request):
    return render(request, 'listings/about-us.html')


def contact(request):
    return render(request, 'listings/contact.html')