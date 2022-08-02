from django.shortcuts import render
from api.models import *

def dashboard(request):
    object = Dori.objects.all()
    return render(request, 'dashboard.html', {'obect':object})

# def datatable(request):
#     objects = ZikrWord.objects.all()
#     counts = Count.objects.all()
#     context = {
#         'counts':counts,
#         'objects':objects
#     }
#     return render(request, 'datatable.html', context)

def mahsulotlar(request):
    objects = Dori.objects.all()
    context = {
        'objects':objects
    }
    return render(request, 'mahsulotlar.html', context)

def mahsulot_add(request):
    if request.method == 'POST':
        nomi = request.POST['nomi']
        rasmi = request.FILES['rasmi']
        tarkibi = request.POST['tarkibi']
        qollanilishi = request.POST['qollanilishi']
        foydalanish_tartibi = request.POST['foydalanish_tartibi']
        Dori.objects.create(
            nomi = nomi,
            rasmi=rasmi,
            tarkibi=tarkibi,
            qollanilishi=qollanilishi,
            foydalanish_tartibi=foydalanish_tartibi
        )
    return render(request, 'mahsulot-add.html')

def mahsulot_detail(request, pk):
    object = Dori.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request, 'mahsulot.html', context)

def yangliklar(request):
    news = Yangiliklar.objects.all()
    context = {
        'news':news
    }

    return render(request, 'news.html', context)

def yanglik(request, pk):
    new = Yangiliklar.objects.get(pk=pk)
    context = {
        'new':new
    }

    return render(request, 'new.html', context)


def linklar(request):
    telegram = TelegramModel.objects.last()
    instagram = InstagramModel.objects.last()
    email = EmaiModel.objects.last()
    phone = TelegramModel.objects.last()
    twitter = TwitterModel.objects.last()
    facebook = FacebookModel.objects.last()
    context = {
        'telegram':telegram,
        'instagram':instagram,
        'email':email,
        'phone':phone,
        'twitter':twitter,
        'facebook':facebook
    }

    return render(request, 'links.html', context)

def staff(request):
    staffs = Staff.objects.all()
    context = {
        'staff':staffs
    }
    return render(request, 'staffs.html', context)

# def about_company(request):
#     pass