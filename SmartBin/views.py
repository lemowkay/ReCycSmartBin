from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
posts = [
     {
          'title': 'Reviews 1',
          'name': 'Gaseledi Mosele',
          'age': 36,
          'date_posted':'20 March 2014',
          'content': '"I love how easy it is to use the smart bin she said. By simply scanning and depositing my waste,/n I earn points that I can redeem for various rewards."' ,  
     },
     {
          'title':'Review 2',
          'name': 'Margaux',
          'age': 28,
          'date_posted':'12 April 2015',
          'content': 'I have always been fascinated by the idea of using technology to make our lives easier. I am really excited about this project and I am looking forward to helping others achieve their goals.' ,
     }
]


def home(request):
     context = {
        'image_url': 'static/img/logo.jpg' ,
        'slogan': 'Revolutionizing waste management and recycling for a greener future.!',
     }
     return render(request, 'home.html', context)

def logout_view(request):
     return render(request, 'users/logout.html')

def about(request):
     return render(request, 'Login.html', {'title': 'About'})

def posts(request):
     return render(request, 'posts.html', {'title': 'Posts'})


def map_view(request):
    return render(request, 'users/map.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def services(request):
    return render(request, 'Services.html')

def userpage(request):
    return render(request, 'users/userpage.html')

def recycleTip(request):
    return render(request, 'users/recycleTip.html')

def rewardpage(request):
    return render(request, 'users/rewardpage.html')

def upload_slip(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # Process the uploaded file here
        return render(request, 'users/upload_slip.html', {'uploaded_file_url': uploaded_file_url})
    else:
        return render(request, 'users/upload_slip.html')  

def scan_view(request):
    context = {
        'bin_code': '1452',
        'date': '2024/02/08',
        'time': '10:52Am',
        'total_weight': '1kg',
    }
    return render(request, 'users/scan.html', context)  

def reward_price(request):
    return render(request, 'users/pricepage.html')

def pickup(request):
    return render(request, 'users/pickup.html')

def pickup_request(request):
    return render(request, 'users/PickupRequest.html')

def pickup_history(request):
    return render(request, 'users/pickupHistory.html')

def pickup_Report(request):
    return render(request, 'users/Report.html')