from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from django.http.request import QueryDict, MultiValueDict
import json
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

def index(request):
    return HttpResponse("hello django")

def about(request):
    return HttpResponse("about get")



def test_post(request):

 #   {% csrf_token  %}

    #name=request.POST
    posted_data = JSONParser().parse(request)
    # email=request.POST.get("my_email")
    print(posted_data["my_name"])
    print(posted_data["my_email"])
    # myDict = dict(name)
    # print(myDict)

    #print(name["my_name"])
    #print(email)
    
    return HttpResponse({"Ok":"200"})

# def test_post(request):
#     if request.method == 'POST':
#         my_data=request.POST
#         print(my_data)
#         data = my_data.json()
#         print(data)
#         return Response({"Ok":"200"})

 
 

