from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
import json
import datetime
from DataBase import DBOPs

from django.http import HttpResponse
from chatbot import aimlKernel


def chat(request):
    """
    Function:
        对话接口
    Args:
        request: 请求
    Returns:
        返回Http报文

    """
    dic = {}
    if request.method == 'GET':
        dic['botResponse'] = aimlKernel.k.respond(request.GET.get('ask', '无语'), request.GET.get('sessionid','test')).\
            replace(' ', '')
        DBOPs.InsertDB(request.GET.get('sessionid', 'test'), request.GET.get('ask', '无语'), dic['botResponse'])
        dic['time'] = datetime.datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))
        dic['sessionid'] = request.GET.get('sessionid','test')
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
    else:
        dic['message'] = u'方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
