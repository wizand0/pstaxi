from django.views.generic import DetailView, ListView
from django.shortcuts import render
from motorpool.forms import SendEmailForm
from django.contrib import messages


from motorpool.models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'motorpool/brand_list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_number'] = Brand.objects.count()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-pk')



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

def send_email_view(request):
    if request.method == 'POST':
        # Если метод запрос POST (нажата кнопка Отправить e-mail),
        # то создаем экземпляр формы с данными из запроса
        form = SendEmailForm(request.POST)
        if form.is_valid():
            # получаем поля формы, прошедшие валидацию
            cd = form.cleaned_data
            email = cd.get('email', '')
            comment = cd.get('comment', '')
            checkbox1 = cd.get('checkbox1', False)
            checkbox2 = cd.get('checkbox2', False)
            variant = int(cd.get('variant', 1))
            variants = cd.get('variants', [])

            action = request.POST.get('btn_action', '')
            if action == 'action1':
                print('Нажата кнопка 1')
            elif action == 'action2':
                print('Нажата кнопка 2')
            else:
                print('Нажата нераспознанная кнопка')
        else:
            messages.error(request, form.non_field_errors())
    else:
        # Если метод запрос GET (страница открыта в браузере),
        # то создаем пустой экземпляр формы
        form = SendEmailForm()

    # Передаем форму в контекст с именем form
    return render(request, 'motorpool/send_email.html', {'form': form})


