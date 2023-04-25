from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm, LoginForm

def index(request):
    item = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': item,
        'categories': category,
    })

def contact(request):
    return render(request, 'core/contact.html')

def terms(request):
    return render(request, 'core/terms.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
    })
