from django.shortcuts import render, HttpResponseRedirect
from .models import *
# from .forms import *
from django.contrib import messages

# Create your views here.


def home(req):
    status = req.session.get('status')
    if req.session.get('cart'):
        cartcount = len(req.session.get('cart'))
    else:
        cartcount = 0
    cart = req.session.get('cart')
    # cartlen=len(cart)

    if cart == None:
        req.session['cart'] = {}
    # print(dict(req.session))       #req.session -- inobject formate
    return render(req, 'app/index.html', {'status': status, 'cartcount': cartcount})


def gallary(req):
    cartcount = len(req.session.get('cart'))
    status = req.session.get('status')
    data = Gallary.objects.all()
    if req.method == "POST":
        id = int(req.POST.get('id'))
        quantity = int(req.POST.get('quantity'))
        reqquantity = int(req.POST.get('reqquantity'))
        # print(id,quantity,reqquantity)
        if reqquantity > quantity:
            msg = "given Quantity not in stock"
            # return render(req, 'app/gallary.html', {'data': data, 'msg': msg, 'id': id, 'status': status,'cartcount': cartcount})
            status = req.session.get('status')
            return HttpResponseRedirect("/gallary/")
        cart = req.session.get('cart')  # local variable
        # print(cart)
        old = cart.get(str(id))
        # print(old)
        if old:
            cart[id] = reqquantity+int(old)
        else:
            cart[id] = reqquantity
        # print(cart)
        req.session['cart'] = cart
        # print(dict(req.session))
        return HttpResponseRedirect("/gallary/")
    return render(req, 'app/gallary.html', {'data': data, 'status': status, 'cartcount': cartcount})


def cart(req):
    status = req.session.get('status')
    cartcount = len(req.session.get('cart'))
    # print(cartcount)
    if req.method == "POST":
        # print(req.POST)
        id = req.POST['id']
        if id and req.POST.get('remove'):
            cart = req.session['cart']
            # print(cart)
            cart.pop(id)
            # print(cart)
            req.session['cart'] = cart
            # print(dict(req.session))
            return HttpResponseRedirect('/cart/')
        updatequantity = req.POST['updatequantity']
        id = req.POST['id']
        # print(updatequantity,id)
        cart = req.session['cart']
        cart[id] = updatequantity
        req.session['cart'] = cart
    cart = req.session.get('cart')
    # print(cart)
    list_final = []
    GT = 0
    for i, j in cart.items():
        id = int(i)
        quantity = int(j)
        # print(id,quantity)
        d = Gallary.objects.get(pk=id)
        price = d.Price
        # print(price)
        total = quantity*price
        # print(total)
        # print(GT)
        lis = [d, quantity, total]
        list_final.append(lis)
        GT += total
    return render(req, 'app/cart.html', {'list_final': list_final, "GT": GT, 'status': status, 'cartcount': cartcount})


def search(req):
    status = req.session.get('status')
    data = Gallary.objects.all()
    if req.method == "POST" and req.POST['search']:
        search = req.POST['search']
        if search:
            data = Gallary.objects.filter(Name__icontains=search)
            # print(data)
            if data:
                return render(req, 'app/gallary.html', {'data': data, 'status': status})
            else:
                msg = "No Matched Data Founds"
                return render(req, 'app/gallary.html', {'msg': msg, 'status': status, 'data': data})
                # return HttpResponseRedirect('/search/')
        else:
            msg = "Blank Entry!!! No Data Founds"
            return HttpResponseRedirect('/search/')
    msg = "No data Founds"
    return render(req, 'app/gallary.html', {'msg': msg, 'status': status, 'data': data, })


def contact(req):
    status = req.session.get('status')
    cartcount = len(req.session.get('cart'))
    cart = req.session.get('cart')
    return render(req, 'app/contact.html', {'status': status, 'cartcount': cartcount})


def payment(req):
    if req.method == "POST":
        if req.user.is_authenticated:  # boolean variable
            user = req.user
            # print(req.user.is_authenticated)
            data = req.session.get('cart')
            print(data)
            for i, j in data.items():
                id = int(i)
                quantity = j
                ins = Transactions(user=user, cat_id=id,
                                   purchased_quan=quantity)
                ins.save()
            req.session['cart'] = {}
            return render(req, 'app/cart.html', {'msg': "Successfully Order"})
        else:
            return HttpResponseRedirect("/auth1/login/")
    return render(req, 'app/cart.html', {'msg': "No Product Available in Your Cart"})
