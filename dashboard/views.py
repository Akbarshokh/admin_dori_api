from django.shortcuts import render
from api.models import *

def dashboard(request):
    object = Dori.objects.all()
    return render(request, 'base.html', {'obect':object})

# def datatable(request):
#     objects = ZikrWord.objects.all()
#     counts = Count.objects.all()
#     context = {
#         'counts':counts,
#         'objects':objects
#     }
#     return render(request, 'datatable.html', context)