from django.shortcuts import render, redirect

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
