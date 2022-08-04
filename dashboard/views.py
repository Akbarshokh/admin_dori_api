from django.shortcuts import redirect, render
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

def mahsulot_list(request):
    objects = Dori.objects.all()
    context = {
        'objects':objects
    }
    return render(request, 'mahsulot-list.html', context)

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
    return render(request, 'mahsulot-detail.html', context)


def yangilik_list(request):
    news = Yangiliklar.objects.all()
    context = {
        'news':news
    }

    return render(request, 'news-list.html', context)


def yanglik_detail(request, pk):
    news = Yangiliklar.objects.get(pk=pk)
    context = {
        'news':news
    }

    return render(request, 'news-detail.html', context)


def yangilik_add(request):
    if request.method == 'POST':
        rasmi = request.FILES['rasmi']
        title = request.POST['title']
        body = request.POST['body']
        
        Yangiliklar.objects.create(
            rasmi=rasmi,
            title = title,
            body=body,
        )
    return render(request, 'news-add.html')


def linklar(request):
    telegram = TelegramModel.objects.last()
    instagram = InstagramModel.objects.last()
    email = EmailModel.objects.last()
    phone = TelefonModel.objects.last()
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

    return render(request, 'link-list.html', context)

def add_link(request):
    return render(request, 'link-add.html')


def add_email(request):
    if request.method == 'POST':
        name = request.POST['name']

        EmailModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


def add_phone(request):
    if request.method == 'POST':
        name = request.POST['name']

        TelefonModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


def add_twitter(request):
    if request.method == 'POST':
        name = request.POST['name']

        TwitterModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


def add_facebook(request):
    if request.method == 'POST':
        name = request.POST['name']

        FacebookModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


def add_telegram(request):
    if request.method == 'POST':
        name = request.POST['name']

        TelegramModel.objects.create(
            name=name
        )
    return redirect('linklar_list')

    
def add_telegram(request):
    if request.method == 'POST':
        name = request.POST['name']

        TelegramModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


def add_instagram(request):
    if request.method == 'POST':
        name = request.POST['name']

        InstagramModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


def staff(request):
    staffs = Staff.objects.all()
    context = {
        'staff':staffs
    }
    return render(request, 'staff-list.html', context)

def staff(request, pk):
    staff = Staff.objects.get(pk=pk)
    context = {
        'staff':staff,
    }

    return render(request, 'staf-detail.html', context)

def staff_add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        kasbi = request.POST['kasbi']
        about = request.POST['about']
        telefon = request.POST['telefon'] 
        telegram = request.POST['telegram'] 
        email = request.POST['email']
        twitter = request.POST['twitter']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']               
        avatar = request.FILES['avatar']
                
        Staff.objects.create(
            first_name=first_name,
            last_name=last_name,
            kasbi=kasbi,
            about=about,
            telefon=telefon,
            telegram=telegram,
            email=email,
            twitter=twitter,
            facebook=facebook,
            instagram=instagram,            
            avatar=avatar,
        )
    return render(request, 'staff-add.html')