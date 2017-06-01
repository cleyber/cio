from django.shortcuts import render

def index(request):
    return render(request, 'webapp/user/index.html')

def index_admin(request):
    return render(request, 'webapp/admin/index.html')

def login(request):
    return render(request, 'webapp/login.html')

def signin(request):
    return render(request, 'webapp/signin.html')

def config(request):
    pass

def schedule(request):
    pass

def users(request):
    return render(request, 'webapp/admin/users.html')

def paysheet(request):
    pass
