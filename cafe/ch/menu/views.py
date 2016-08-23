from django.shortcuts import render
from menu.models import Cafe, Coffee
import json
from django.http import HttpResponse, JsonResponse

def index(request):
    cafe_list = Cafe.objects.all()
    datalist={}
    coffeelist={}
    for cafe in cafe_list:
        for coffee in cafe.coffee_set.all():
            coffeelist.update({coffee.coffee_name: coffee.coffee_price})
        datalist.update(
                            {
                                cafe.cafe_name: {
                                    'data': {
                                        'cafe_name':cafe.cafe_name,'cafe_color':cafe.cafe_color, 'cafe_menu':coffeelist
                                    }
                                }
                            }
                        )
        #coffeelist={}
    return HttpResponse(json.dumps(datalist), content_type='application/json')





def index2(request):
    cafe_list = Cafe.objects.all()
    return render(request, 'menu/index.html', {'cafe_list': cafe_list})
    
