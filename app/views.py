from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies,Tvshows1,Category,Seasons,Episodes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.db.models import Q





def index(request):
            query = request.GET.get('search')
            if query:
                        results = Movies.objects.filter(name__icontains=query)
            else:
                                        results = Movies.objects.all() 
            return render(request, 'app/index.html',{ 'movies': results})







                            





