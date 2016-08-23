from django.shortcuts import render
from menu.models import Cafe, Coffee
import json
from django.http import HttpResponse, JsonResponse

def index(request):
    cafe_list = Cafe.objects.all()
    datalist={}
    for cafe in cafe_list:
        for coffee in cafe.coffee_set.all:
            datalist.update
            (
                    {
                    cafe.cafe_name:
                        {
                            'data':
                                {
                                'cafe_name':cafe.cafe_name,
                                'cafe_color':cafe.cafe_color,
                                'cafe_menu':
                                    {
                                    coffee_name:
                                            {
                                            'coffee_name':coffee.coffee_name,
                                            'coffee_price':coffee.coffee_price
                                            }
                                    }
                                }
                        }
                    
                    }
            )
    #for cafe in cafe_list:
        #data.update({cafe.cafe_name: {'data': {'cafe_name':cafe.cafe_name,'cafe_color':cafe.cafe_color}}})
    #json_data = {'data':data} 
    return HttpResponse(json.dumps(datalst), content_type='application/json')





def index2(request):
    cafe_list = Cafe.objects.all()
    return render(request, 'menu/index.html', {'cafe_list': cafe_list})
    
