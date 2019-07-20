from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import sys, os
import requests

from .models import *

			


@csrf_exempt
def ke(request):
    jsob={}
    log=[]
    if request.method == "POST":
        try:
            data = request.POST["data"]
            received = json.loads(data)
            jsob.update(received)
            num_list = jsob["int number"]
            num = num_list.split(",",-1)
            i = 0
            result = ""
            final = []
            for i in range(len(num)):
                a = int(num[i])
                while a:
                    pro = a % 2
                    a = a // 2
                    log.append(pro)
                while log:
                    result += str(log.pop())
                i=i+1
                final.append(result)
            return JsonResponse({"10 to 2": final})

 
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return HttpResponse("<h1>ONLY POST REQUESTS</h1>")



@csrf_exempt
def AAA1(request):
    jsob={}
    log=[]
    if request.method == "POST":
        try:
            data = request.POST["data"]
            received = json.loads(data)
            jsob.update(received)
            cityname = jsob["cityname"]
            url = "http://web.juhe.cn:8080/environment/air/cityair?city={}&key=06f31e4bbc44443078083457a8b7a0c8".format(cityname)
            response = requests.get(url).text
            air = {}
            air = json.loads(response)
            log = air["result"]
            log = log[0]
            air = log["citynow"] 
            log = air["AQI"]

            return JsonResponse("AQI: %s" % log ,safe=False)
            
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return HttpResponse("<h1>ONLY POST REQUESTS</h1>")




