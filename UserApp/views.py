from django.shortcuts import render,redirect
from SellerApp.models import *
from AdminApp.models import *
from UserApp.models import *
from django.db.models import Q
def Home(request):
    return render(request, 'home.html')

def Shop(request):
    products = Product.objects.all()

    if request.method == 'POST':
        name = request.POST.get('search')
        products = Product.objects.filter(Q(product_name__icontains=name)|Q(brand_name__icontains=name))
    return render(request, 'shop.html', {'products': products})

def Men(request):
    products = Product.objects.filter(main_category_id=1)

    if request.method == 'POST':
        name = request.POST.get('search')
        products = Product.objects.filter(Q(product_name__icontains=name) | Q(brand_name__icontains=name))
        products = products.filter(main_category_id=1)
    return render(request, 'men.html', {'data': products})

def Women(request):
    products = Product.objects.filter(main_category_id=2)

    if request.method == 'POST':
        name = request.POST.get('search')
        products = Product.objects.filter(Q(product_name__icontains=name) | Q(brand_name__icontains=name))
        products = products.filter(main_category_id=2)
    return render(request, 'women.html', {'new': products})

def Kids(request):
    products = Product.objects.filter(main_category_id=3)

    if request.method == 'POST':
        name = request.POST.get('search')
        products = Product.objects.filter(Q(product_name__icontains=name) | Q(brand_name__icontains=name))
        products = products.filter(main_category_id=3)
    return render(request, 'kids.html', {'index': products})

def User_Login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')

        users = UserDetails.objects.filter(user_name=user_name, password=user_password)

        if users.exists():
            user = users.first()
            request.session['user'] = user.user_id
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
     return render(request, 'login.html')

def User_Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        if UserDetails.objects.filter(user_name=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        userdata = UserDetails()
        userdata.user_name = username
        userdata.password = password
        userdata.phone_number = phone_number
        userdata.save()
        return redirect('/userlogin')
    return render(request, 'signup.html')


def Contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')

def Buynow(request,id):
    products = Product.objects.filter(product_id=id)
    return render(request, 'buy_now.html', {'items': products})
def Add_Cart(request, product_id):
    if 'user' in request.session:
        user_id = request.session['user']
        existing_item = Cart_Item.objects.filter(user_id=user_id, product_id=product_id).exists()
        if not existing_item:
            Cart_Item.objects.create(user_id=UserDetails.objects.get(user_id=user_id),
                                    product_id=Product.objects.get(product_id=product_id))
        return redirect('/cart')
    else:
        return redirect('/')

def Cart(request):
    if 'user' in request.session:
        user = request.session['user']
        cartdata = Cart_Item.objects.filter(user_id=user)
        return render(request, "add_cart.html", {'cart_items': cartdata})
    else:
        return redirect('/')

def Remove_Cart(request,product_id):
    item = Cart_Item.objects.get(product_id=product_id)
    item.delete()
    return redirect('/cart')



def Add_Wishlist(request, product_id):
        if 'user' in request.session:
            user_id = request.session['user']
            existing_item = WishlistItem.objects.filter(user_id=user_id, product_id=product_id).exists()
            if not existing_item:
                WishlistItem.objects.create(user_id=UserDetails.objects.get(user_id=user_id),
                                            product_id=Product.objects.get(product_id=product_id))
            return redirect('/wishlist')
        else:
            return redirect('/')

def Wishlist(request):
    if 'user' in request.session:
        user = request.session['user']
        wishdata = WishlistItem.objects.filter(user_id=user)
        return render(request, "wishlist.html", {'wishlist_items': wishdata})
    else:
        return redirect('/')


def Remove_Wishlist(request,product_id):
    item = WishlistItem.objects.get(product_id=product_id)
    item.delete()
    return redirect('/wishlist')
