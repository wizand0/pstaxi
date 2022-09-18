from django.views.generic import DetailView


def brand_list(request):
    template_name = 'motorpool/brand_list.html'
    brand_objects = Brand.objects.all()
    brand_number = brand_objects.count()
    context = {
        'brand_objects': brand_objects,
        'brand_number': brand_number,
    }

    return render(request, template_name, context)


class BrandDetailView(DetailView):
    model = Brand

