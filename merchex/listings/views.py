from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    listings = Listing.objects.all()
    context = {
        'bands': bands,
        'listings': listings,
    }
    return render(request, 'listings/hello.html', context)

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons le merch !</p>')