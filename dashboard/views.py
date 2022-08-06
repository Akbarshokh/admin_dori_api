from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from api.models import *

@login_required(login_url='login_url')
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


@login_required(login_url='login_url')
def mahsulot_list(request):
    objects = Dori.objects.all()
    context = {
        'objects':objects
    }
    return render(request, 'mahsulot-list.html', context)


@login_required(login_url='login_url')
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



@login_required(login_url='login_url')
def mahsulot_detail(request, pk):
    object = Dori.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request, 'mahsulot-detail.html', context)

@login_required(login_url='login_url')
def mahsulot_update(request):    
    nomi = request.POST['nomi']
    tarkibi = request.POST['tarkibi']
    qollanilishi = request.POST['qollanilishi']
    foydalanish_tartibi = request.POST['foydalanish_tartibi']    
    rasmi = request.FILES.get('rasmi')
    id = request.POST['prod_id']

    update_object = Dori.objects.get(id=id)
    update_object.nomi = nomi
    update_object.tarkibi = tarkibi
    update_object.qollanilishi = qollanilishi
    update_object.foydalanish_tartibi = foydalanish_tartibi
    
    if rasmi is not None:
        update_object.rasmi = rasmi
    
    update_object.save()
    
    return redirect('mahsulot_detail', id)
        
@login_required(login_url='login_url')        
def mahsulot_delete(request):
    if request.method == 'POST':
        prod_id =  request.POST['prod_id']
        delete_product = Dori.objects.get(id=prod_id)
        delete_product.delete()
        return redirect('mahsulot_list')


@login_required(login_url='login_url')
def yangilik_list(request):
    news = Yangiliklar.objects.all()
    context = {
        'news':news
    }
    return render(request, 'news-list.html', context)


@login_required(login_url='login_url')
def yanglik_detail(request, pk):
    news = Yangiliklar.objects.get(pk=pk)
    context = {
        'news':news
    }
    return render(request, 'news-detail.html', context)


@login_required(login_url='login_url')
def yangilik_update(request):    
    title = request.POST['title']
    body = request.POST['body']
    rasmi = request.FILES.get('rasmi')
    id = request.POST['prod_id']

    update_object = Yangiliklar.objects.get(id=id)
    update_object.title = title
    update_object.body = body
    
    if rasmi is not None:
        update_object.rasmi = rasmi
    
    update_object.save()
    
    return redirect('yangilik_detail', id)
        
@login_required(login_url='login_url')        
def yangilik_delete(request):
    if request.method == 'POST':
        prod_id =  request.POST['prod_id']
        delete_product = Yangiliklar.objects.get(id=prod_id)
        delete_product.delete()
        return redirect('yangilik_list')
    
    

@login_required(login_url='login_url')
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


@login_required(login_url='login_url')
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


@login_required(login_url='login_url')
def add_link(request):
    return render(request, 'link-add.html')

@login_required(login_url='login_url')
def add_map(request):
    if request.method == 'POST':
        map = request.POST['map']

        Map.objects.create(
            map=map,
        )        
        
    return render(request, 'location.html')



@login_required(login_url='login_url')
def map_detail(request, pk):
    map = Map.objects.get(pk=pk)
    context = {
        'map':map
    }
    return render(request, 'location-list.html', context)

@login_required(login_url='login_url')
def add_email(request):
    if request.method == 'POST':
        name = request.POST['name']

        EmailModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


@login_required(login_url='login_url')
def add_phone(request):
    if request.method == 'POST':
        name = request.POST['name']

        TelefonModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


@login_required(login_url='login_url')
def add_twitter(request):
    if request.method == 'POST':
        name = request.POST['name']

        TwitterModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


@login_required(login_url='login_url')
def add_facebook(request):
    if request.method == 'POST':
        name = request.POST['name']

        FacebookModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


@login_required(login_url='login_url')
def add_telegram(request):
    if request.method == 'POST':
        name = request.POST['name']

        TelegramModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


@login_required(login_url='login_url')    
def add_telegram(request):
    if request.method == 'POST':
        name = request.POST['name']

        TelegramModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


@login_required(login_url='login_url')
def add_instagram(request):
    if request.method == 'POST':
        name = request.POST['name']

        InstagramModel.objects.create(
            name=name
        )
    return redirect('linklar_list')


@login_required(login_url='login_url')
def staff(request):
    staff = Staff.objects.all()
    context = {
        'staff':staff
    }
    return render(request, 'staff-list.html', context)


@login_required(login_url='login_url')
def staff_detail(request, pk):
    staff = Staff.objects.get(pk=pk)
    context = {
        'staff':staff
    }
    return render(request, 'staff-detail.html', context)


@login_required(login_url='login_url')
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

@login_required(login_url='login_url')
def staff_update(request): 
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
    avatar = request.FILES.get('avatar')
    id = request.POST['prod_id']

    update_object = Staff.objects.get(id=id)
    update_object.first_name = first_name
    update_object.last_name = last_name
    update_object.kasbi = kasbi
    update_object.about = about
    update_object.telefon = telefon
    update_object.telegram = telegram
    update_object.email = email
    update_object.twitter = twitter
    update_object.facebook = facebook
    update_object.instagram = instagram
    
    if avatar is not None:
        update_object.avatar = avatar
    
    update_object.save()
    
    return redirect('staff_detail', id)
        
        
@login_required(login_url='login_url')        
def staff_delete(request):
    if request.method == 'POST':
        prod_id =  request.POST['prod_id']
        delete_product = Staff.objects.get(id=prod_id)
        delete_product.delete()
        return redirect('staff_list')


@login_required(login_url='login_url')
def text(request):
    text = WebsiteText.objects.all()
    context = {
        'text':text
    }
    return render(request, 'company-list.html', context)


@login_required(login_url='login_url')
def text_detail(request, pk):
    text = WebsiteText.objects.get(pk=pk)
    context = {
        'text':text
    }
    return render(request, 'company-detail.html', context)


@login_required(login_url='login_url')
def text_add(request):
    if request.method == 'POST':        
        title = request.POST['title']
        body = request.POST['body']        
        
        WebsiteText.objects.create(            
            title = title,
            body = body,
            
        )
        
    return render(request, 'company-add.html')

@login_required(login_url='login_url')
def text_update(request): 
    title = request.POST['title']       
    body = request.POST['body']    
    id = request.POST['prod_id']

    update_object = WebsiteText.objects.get(id=id)
    update_object.title = title
    update_object.body = body   
               
    update_object.save()
    
    return redirect('text-comments-detail', id)
        
        
@login_required(login_url='login_url')        
def text_delete(request):
    if request.method == 'POST':
        prod_id =  request.POST['prod_id']
        delete_product = WebsiteText.objects.get(id=prod_id)
        delete_product.delete()
        return redirect('text-comment-detail')
#delete view
# def delete_note(request, pk=None):
#     Notes.objects.get(id=pk).delete()
#     return redirect("notes")


@login_required(login_url='login_url')
def feedback_list(request):
    feedback = Feedback.objects.order_by('-id')
    context = {
        'feedback':feedback
    }
    return render(request, 'feedback-list.html', context)


@login_required(login_url='login_url')
def feedback_detail(request, pk):
    feedback = Feedback.objects.get(pk=pk)
    context = {
        'feedback':feedback
    }
    return render(request, 'feedback-detail.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard_url')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'login.html')


def logout_view(request):
        logout(request)
        return redirect("login_url")
    
    
@login_required(login_url='login_url')
def comment_image_list(request):
    image = CommentImageModel.objects.all()
    context = {
        'image':image
    }
    return render(request, 'image-comment-list.html', context)


@login_required(login_url='login_url')
def comment_image_detail(request, pk):
    text = WebsiteText.objects.get(pk=pk)
    context = {
        'text':text
    }
    return render(request, 'image-comment-detail.html', context)


@login_required(login_url='login_url')
def comment_image_add(request):
    if request.method == 'POST':        
        image = request.POST['title']
              
        
        CommentImageModel.objects.create(            
            title = title,
            
            
        )
        
    return render(request, 'image-comment-add.html')

@login_required(login_url='login_url')
def comment_image_update(request): 
    image = request.POST['image']       
      
    id = request.POST['prod_id']

    update_object = CommentImageModel.objects.get(id=id)
    update_object.image = image
      
               
    update_object.save()
    
    return redirect('image-comment-detail', id)
        
        
@login_required(login_url='login_url')        
def comment_image_delete(request):
    if request.method == 'POST':
        prod_id =  request.POST['prod_id']
        delete_product = CommentImageModel.objects.get(id=prod_id)
        delete_product.delete()
        return redirect('image-comment-list')
    
    
    
@login_required(login_url='login_url')
def text_comment(request):
    text = CommentModel.objects.all()
    context = {
        'text':text
    }
    return render(request, 'text-comment-list.html', context)


@login_required(login_url='login_url')
def text_comment_detail(request, pk):
    text = CommentModel.objects.get(pk=pk)
    context = {
        'text':text
    }
    return render(request, 'text-comment-detail.html', context)


@login_required(login_url='login_url')
def text_comment_add(request):
    if request.method == 'POST':        
        title = request.POST['title']
        body = request.POST['body']        
        
        CommentModel.objects.create(            
            title = title,
            body = body,
            
        )
        
    return render(request, 'text-comment-add.html')

@login_required(login_url='login_url')
def text_comment_update(request): 
    title = request.POST['title']       
    body = request.POST['body']    
    id = request.POST['prod_id']

    update_object = CommentModel.objects.get(id=id)
    update_object.title = title
    update_object.body = body   
               
    update_object.save()
    
    return redirect('text_comment_update', id)
        
        
@login_required(login_url='login_url')        
def text_comment_delete(request):
    if request.method == 'POST':
        prod_id =  request.POST['prod_id']
        delete_product = CommentModel.objects.get(id=prod_id)
        delete_product.delete()
        return redirect('text_comment_delete')