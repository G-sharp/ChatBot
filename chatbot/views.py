from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
import json
import datetime
from django.http import HttpResponse
from chatbot import aimlKernel

def chat(request):
    dic = {}
    if request.method == 'GET':
        dic['botResponse'] = aimlKernel.k.respond(request.GET.get('ask', '无语'),request.GET.get('sessionid','test')).replace(' ', '')
        dic['time'] = datetime.datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
        dic['sessionid'] = request.GET.get('sessionid','test')
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
    else:
        dic['message'] = u'方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
