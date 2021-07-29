from django.shortcuts import render, redirect
from .models import Product
from .forms import AddItemForm
from .filters import ProductFilter

def Index(request):

    if request.user.is_authenticated:
        user = request.user

        products = Product.objects.filter(user = user)

        myFilter = ProductFilter(request.GET, queryset = products)

        products = myFilter.qs

        data = {
            'products': products,
            'myFilter': myFilter,
        }

        return render(request, 'index.html', data)
    
    else:
        return render(request, 'index.html')

def Additem(request):

    if request.method == 'POST':
        user = request.user
        form = AddItemForm(request.POST)
        #confirm = False

        if form.is_valid():
            additem = form.save(commit = False)
            additem.user = user
            additem.save()

            #confirm = True

            return redirect('home')
        
        else:
            return render(request, 'additem.html', form)

    else:

        if request.user.is_authenticated:
            user = request.user
            form = AddItemForm()    

            return render(request, 'additem.html', {'form': form})
        
        else:
            return render(request, 'additem.html')

def Deleteitem(request, id):
    Product.objects.get(pk = id).delete()
    return redirect('home')

def Updateitem(request, id):
    obj = Product.objects.get(pk=id)
    form = AddItemForm(request.POST or None, instance=obj)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True    
        
    data = {
        'obj': obj,
        'form': form,
        'confirm': confirm
    }

    return render(request, 'updateitem.html', data)


def Savedlist(request):
    if request.user.is_authenticated:
        user = request.user

        products = Product.objects.filter(user = user)

        data = {
            'products': products,
        }

        return render(request, 'savedlist.html', data)
    
    else:
        return render(request, 'savedlist.html')