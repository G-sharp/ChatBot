from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from chatbot import aimlKernel

def chat(request):
    dic = {}
    if request.method == 'GET':
        dic['botResponse'] = aimlKernel.k.respond(request.GET.get('ask', '无语')).replace(' ', '')
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
    else:
        dic['message'] = u'方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
