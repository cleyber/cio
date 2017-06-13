from django.shortcuts import render
from forms import SignIn

def index(request):
    return render(request, 'webapp/user/index.html')

def index_admin(request):
    return render(request, 'webapp/admin/index.html')

def login(request):
    return render(request, 'webapp/login.html')

def signin(request):
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            return render(request, 'webapp/login.html')
    else:
        form = SignIn
    return render(request, 'webapp/signin.html', {'from': form,})

def config(request):
    pass

def schedule(request):
    pass

def users(request):
    return render(request, 'webapp/admin/users.html')

def paysheet(request):
    pass
