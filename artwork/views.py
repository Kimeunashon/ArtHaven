from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Artwork

def artwork_list(request):
    artworks = Artwork.objects.all()
    return render(request, 'artwork/artwork_list.html', {'artworks': artworks})
