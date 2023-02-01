from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .models import Band, Listing
from .forms import ContactUsForm, BandForm, ListingForm

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

def band_listing_list(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    band_listings = Listing.objects.filter(band=band)
    print(band_listings)
    context = {
        'band': band,
        'band_listings': band_listings,
    }
    return render(request, 'listings/band_listing_list.html', context)

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
        return redirect('band-detail', band.id)

    else:
        form = BandForm()
    context = {
        'form': form,
    }
    return render(request, 'listings/band_create.html', context)

def band_update(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)

    else:
        form = BandForm(instance=band)

    context = {
        'form': form,
    }
    return render(request, 'listings/band_update.html', context)

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'listings/listing_list.html', context)

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    band = listing.band
    context = {
        'band': band,
        'listing': listing,
    }
    return render(request, 'listings/listing_detail.html', context)

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
        return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()
    context = {
        'form': form,
    }
    return render(request, 'listings/listing_create.html', context)

def about(request):
    return render(request, 'listings/about.html')


def contact(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['yoann@test.com']
            )
            return redirect('email-sent')

    else:
        form = ContactUsForm()

    context = {
        'form': form
    }
    return render(request, 'listings/contact.html', context)

def email_sent(request):
    return render(request, 'listings/email_sent.html')