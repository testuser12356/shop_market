import shop.models as models


def variables(request):
    context = {
        "last_products": models.Product.objects.all()[:8],
        "category_list": models.ProductCategory.objects.filter(parent=None),
        "category_children": models.ProductCategory.objects.filter(parent__isnull=False)
    }
    if request.user.is_authenticated:
        if models.Cart.objects.filter(user=request.user, is_active=True).exists():
            cart = {
                "has_cart": True,
                "total_cart_item": models.Cart.objects.filter(user=request.user,
                                                              is_active=True).last().items.all().count(),
                "total_cart_sum": models.Cart.objects.filter(user=request.user, is_active=True).last().total_sum,
            }
            context = context | cart
        else:
            context = context | {"has_cart": False}
    return context
