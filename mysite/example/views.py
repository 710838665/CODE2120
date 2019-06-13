from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import sys, os

from .models import *

# Create your views here.

def example_get(request, var_a, var_b):
	log = []
	try:
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
	log = []
	jsob = {"demo": "12345", "var": "count: "}
	if request.method == "POST":
		try:
			data = request.POST["data"]
			log.append(data)
			received = json.loads(data)
			jsob.update(received)

			index = 0
			for i in jsob["demo"]:
				index = index + 1
				
			index = jsob["var"]+str(index)

			return JsonResponse({"count":index})
		except:
			pass
			


@csrf_exempt
def fib(request):
	log = []
	jsob = {"startnumber": 0, "length": 10}
	if request.method == "POST":
		try:
			data = request.POST["data"]
			log.append(data)
			received = json.loads(data)
			jsob.update(received)




			startnumber = int(jsob["startnumber"])
			length      = int(jsob["length"])
			loop        = range(length)

			numarray    = []
			fibno       = startnumber
			addno       = 1

			for el in loop:
				numarray.append(fibno)
				fibno = fibno+addno
				addno = fibno-addno


			return JsonResponse({"count":numarray})

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")