from django.shortcuts import render
from django.views.generic import DetailView

from motorpool.models import Brand


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
    template_name = 'motorpool/brand_detail.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        default_object = super().get_object(queryset)
        return default_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = self.object.cars.all()
        return context

    def get_template_names(self):
        default_template_names = super().get_template_names()
        return default_template_names



