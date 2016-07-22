from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render

def news_list(request):
    # raise NotImplementedError
    #return HttpResponse("Hola Mundo")
    return render_to_response("news/news_list.html")
