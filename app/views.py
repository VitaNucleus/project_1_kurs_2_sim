from django.shortcuts import render
from .models import River


def river_segment(request):
    if request.method == 'GET':
        return render(request, 'river_segment.html')

    if request.method == 'POST':
        min_area = float(request.POST.get('min_area', 50))
        max_area = float(request.POST.get('max_area', 100))
        min_price = float(request.POST.get('min_price', 0))
        max_price = float(request.POST.get('max_price', 100000))
        rent = request.POST.get('rent', False)

        selected_rivers = River.objects.filter(area__range=(min_area, max_area), price__range=(min_price, max_price))

        if rent:
            selected_rivers = selected_rivers.filter(rent=True)

        average_price = selected_rivers.aggregate(avg_price=Avg('price'))['avg_price']

        return render(request, 'result.html', {'average_price': average_price})