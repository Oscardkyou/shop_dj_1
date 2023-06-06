from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm, CategoryForm, CommentForm, UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def IndexView(request):
      return render(request, 'main/index.html')


def ProductView(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main/product.html', context=context)


def AddProductView(request):
      if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request, "Продукты успешно добавлены!")
            else:
                  messages.error(request, form.errors)
      else:
            form = ProductForm()

      context = {
            'form': form
      }

      return render(request, 'main/addproduct.html', context=context)


def CategoryView(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'main/category.html', context=context)


def CommentView(request):
    products = Product.objects.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = Product.objects.get(pk=request.POST['product_id'])
            comment.save()
            form = CommentForm()

    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'main/product.html', context=context)


def LogoutUserView(request):
    logout(request)
    return redirect('/')


def SignUpUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password != request.POST.get('password2'):
                messages.error(request, "Пароли не совпадают!")
                return redirect('/singup')
            else:
                user.set_password(user.password)
                form.save()
                messages.success(request, "Региcтрация прошла успешна!")
                redirect("/")
    else:
        form = UserForm()
    return render(request, "AuthentificateUser/singup.html", {"form": form})


def SingInUserView(request):
    messages.success(request, 'Thank you for still being with us')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно вошли в свой ЛК")
            return redirect('/')
        else:
            messages.error(request, "Неверный пароль")
            return redirect('/singin')
    else:
        return render(request, "AuthentificateUser/singin.html")


