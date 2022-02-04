from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.models import Band
from listings.models import Listing

from listings.forms import BandForm, ListingForm, ContactUsForm


def hello(request):
    bands = Band.objects.all()
    return render(request,
     'listings/hello.html',
    #  Passer un objet précis
    # {'first_band': bands[0]},
    #  Passer une colelction d'objet
    {'bands': bands})

# Views Bands

def band_list(request):
    bands = Band.objects.all()
    return render(request,
     'listings/band_list.html',
    #  Passer un objet précis
    # {'first_band': bands[0]},
    #  Passer une colelction d'objet
    {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id) # band_id -> Possible de mettre band_id en fonction du model
    return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous passons l'id au modèle

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band_list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})


# End Views Bands

# Views listings

def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
     'listings/listing_list.html',
    #  Passer un objet précis
    # {'first_listing': listings[0]},
    #  Passer une colelction d'objet
    {'listings': listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id) # listing_id -> Possible de mettre listing_id en fonction du model
    return render(request,
          'listings/listing_detail.html',
          {'listing': listing}) # nous passons l'id au modèle

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Listing » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request,
                'listings/listing_update.html',
                {'form': form})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        listing.delete()
        # rediriger vers la liste des groupes
        return redirect('listing_list')

    return render(request,
        'listings/listing_delete.html',
        {'listing': listing})

# End Views listings

def contact(request):
  # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
  print('La méthode de requête est : ', request.method)
  print('Les données POST sont : ', request.POST)

  if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
     form = ContactUsForm(request.POST)

     if form.is_valid():
        send_mail(
          subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
          message=form.cleaned_data['message'],
          from_email=form.cleaned_data['email'],
          recipient_list=['pierre.pocheron@gmail.com'],
        )
        return redirect('email-sent')
  else:
  # ceci doit être une requête GET, donc créer un formulaire vide
      form = ContactUsForm()

  return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit


def email_sent(request):
    return render(request, 'listings/email_sent.html',)


def about(request):
    return HttpResponse('<p>aa</p>')
