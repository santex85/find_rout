from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.models import City


def home(request, pk=None):
    if pk:
        city = get_object_or_404(City, id=pk)
        context = {'object': city}
        return render(request, 'cities/detail.html', context)

    cities = City.objects.all()
    context = {'objects_list': cities}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
