from django.shortcuts import render,redirect
#from model_app.models import User,Message,MessageForm,UserForm
#from django.contrib.auth.forms import UserCreationForm,UserAuthenticationForm
from django.contrib.auth import login,authenticate
from .models import ProductForm, ProductSourceForm,Product

def MP(request):
    return render(request, "MP.html")

def Catalog(request):
    products = Product.objects.all()
    return render(request, "Catalog.html",{'products': products })

def Shopping_cart(request):
    return render(request, "Shopping_cart.html")

def InputProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    form = ProductForm()
    return render(request, 'InputProduct.html', {'form': form })



def InputProductSours(request):
    if request.method == "POST":
        form = ProductSourceForm(request.POST)
        if form.is_valid():
            form.save()


    form = ProductSourceForm()
    return render(request, 'InputProductSours.html', {'form': form })

# def posts(request):
#
#     if request.method == "POST":
#         form = MessageForm(request.POST)
#         user = request.user
#         if form.is_valid() and user.is_authenticated:
#             instance = form.save(commit=False)
#             instance.user = user
#             instance.save()
#         return redirect("/posts")
#     form = MessageForm()
#
#     users = User.objects.all()
#     msgs = Message.objects.select_related('user').all()
#     for m in msgs:
#         print()
#     data = {
#         'users': users,
#         'msgs': msgs,
#         'form': form,
#     }
#     return render(request,"posts.html",data)
#
#
def user(request):
    pass
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # form = UserForm()
    #
    # users = User.objects.all()
    # msgs = Message.objects.select_related('user').all()
    # for m in msgs:
    #     print()
    # data = {
    #     'users': users,
    #     'msgs': msgs,
    #     'form': form,
    # }
    #
    # return render(request,"user.html",data)
#
# def index(request):
#     return render(request, "index.html")
#
# def register(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("/")
#     else:
#         form = UserCreationForm()
#     return render(request,"register.html",{"form":form})

# def sign_in(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request.POST)
#         user = authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:():
#             login(request, user)
#             return redirect("/")
#     else:
#         form = AuthenticationForm()
#     return render(request,"login.html",{"form":form})
#
# def exit(request):
#     logout(request)
#     return redirect("/")