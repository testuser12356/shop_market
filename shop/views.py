from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

import shop.models as models


# Create your views here.


def home(request):
    categories = models.ProductCategory.objects.filter(parent=None)
    last_news = models.News.objects.all()[:6]
    brands = models.Brand.objects.all()
    return render(
        request, "index.html",
        context={
            "categories": categories,
            "last_news": last_news,
            "brands": brands
        }
    )


def product_list(request, category_id):
    object_list = models.Product.objects.all()
    object_list = object_list.filter(category_id=category_id)

    return render(request, "product.html", context={"object_list": object_list})


def product_filter(request):
    object_list = models.Product.objects.all()

    if "category" in request.GET:
        category = request.GET.get("category", None)
        if category != "":
            object_list = object_list.filter(category_id=category)
    if "search" in request.GET:
        search = request.GET.get("search", None)
        object_list = object_list.filter(title__icontains=search)

    return render(request, "product_filter.html", context={"object_list": object_list})


def add_to_favorite(request):
    if request.user.is_authenticated:
        if request.POST:
            product_id = request.POST.get("product")
            user = request.user
            models.Favorite.objects.create(
                user=user,
                product_id=product_id
            )
            return redirect("/")


def create_cart(request, product_id, quantity):
    if request.user.is_authenticated:
        carts = models.Cart.objects.filter(user=request.user, is_active=True)
        price = models.Product.objects.get(id=product_id).price
        t_sum = quantity * price
        if carts.exists():
            cart = carts.last()
            models.CartItem.objects.create(
                cart=cart,
                product_id=product_id,
                quantity=quantity,
                sum=t_sum
            )
            cart.save()
        else:
            cart = models.Cart.objects.create(user=request.user)
            models.CartItem.objects.create(
                cart=cart,
                product_id=product_id,
                quantity=quantity,
                sum=t_sum
            )
            cart.save()
        messages.success(request, "Cart Item qo'shildi")
        return redirect("/")
    else:
        messages.error(request, "Siz login bolmagansiz")
        return redirect("/")


def create_order(request):
    if request.user.is_authenticated:
        cart = models.Cart.objects.filter(user=request.user, is_active=True).first()

        if not cart:
            return HttpResponse("No active cart")

        order = models.Order.objects.create(
            client=request.user,
            cart=cart,
            total_sum=cart.total_sum
        )

        for item in cart.items.all():
            models.OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
                sum=item.sum
            )
        cart.is_active = False
        cart.save()
        return redirect(f"/order/detail/{order.id}")


def order_detail(request, pk):
    order = get_object_or_404(models.Order, pk=pk)
    return render(request, "checkout.html", {"order": order})


def product_detail(request, pk):
    obj = models.Product.objects.get(pk=pk)
    related_products = models.Product.objects.filter(category=obj.category)
    return render(request,
                  "product_single.html",
                  {"object": obj, "related_products": related_products})


def create_billing_info(request):
    ...
