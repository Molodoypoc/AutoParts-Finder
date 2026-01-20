from django.shortcuts import render
from django.views import View
from django.db import models
from .models import Part, CarModel
from .forms import VinSearchForm
from .services import get_parts_analytics  # Функция с Pandas, которую мы наметили ранее


class PartSearchView(View):
    """Контроллер для поиска запчастей по VIN"""
    template_name = 'parts/search.html'

    def get(self, request):
        form = VinSearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = VinSearchForm(request.POST)
        results = None
        car_info = None

        if form.is_valid():
            vin = form.cleaned_data['vin']
            vin_prefix = vin[:9]  # Берем префикс для идентификации модели

            try:
                car = CarModel.objects.get(vin_prefix=vin_prefix)
                car_info = car

                results = Part.objects.filter(compatible_with=car).order_by('price')
            except CarModel.DoesNotExist:
                form.add_error('vin', 'Модель автомобиля с таким VIN-префиксом не найдена.')

        return render(request, self.template_name, {
            'form': form,
            'results': results,
            'car_info': car_info
        })


class AnalyticsView(View):

    template_name = 'parts/analytics.html'

    def get(self, request):

        stats = get_parts_analytics()

        context = {
            'stats': stats,
            'total_count': Part.objects.count(),
            'max_price': Part.objects.aggregate(models.Max('price'))['price__max']
        }
        return render(request, self.template_name, context)
