from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({"title":"blog",
                         "content":"this is sample content",
                         "data":{"name":"Saul",
                                 "age":29,
                                 "location":"USA"}})