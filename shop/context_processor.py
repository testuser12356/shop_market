import shop.models as models


def variables(request):
    return {
        "last_products": models.Product.objects.all()[:8],
        "category_list": models.ProductCategory.objects.filter(parent=None),
        "category_children": models.ProductCategory.objects.filter(parent__isnull=False)
    }
