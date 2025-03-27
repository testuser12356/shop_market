import shop.models as models


def variables(request):
    return {
        "category_list": models.ProductCategory.objects.filter(parent=None),
    }
