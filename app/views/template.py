# -*- coding: utf-8 -*-
# Created by: Leemon7
# Created on: 2021/11/9
# Function:

from sanic import Sanic
from sanic.response import json, html, redirect
from sanic.views import HTTPMethodView
from sanic.log import logger, error_logger, access_logger
from app.models import EmailSite
from sanic.handlers import ErrorHandler


async def index(request):
    # print(request)
    # return html('<h1>hello world!</h1>')
    app = Sanic.get_app('__main__')
    url = app.url_for('v2.TemplateViews')
    return redirect(url)


async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = ws.recv()
        print('Received: ' + data)


class TemplateViews(HTTPMethodView):
    async def post(self, request, *args, **kwargs):
        logger.info(request.form)
        data = EmailSite.create(site_id=request.form.get('site_id'),
                                site_type=request.form.get('site_type'),
                                site_name=request.form.get('site_name'),
                                api_url=request.form.get('api_url'),
                                special=request.form.get('special'),
                                )
        return json({
            "code": 1,
            "msg": "successful",
            "data": {'id': data.id,
                     'site_id': data.site_id,
                     'site_type': data.site_type,
                     'site_name': data.site_name,
                     'api_url': data.api_url,
                     'special': data.special}
        })

    async def get(self, request, *args, **kwargs):
        logger.info("get site list.")
        query_dict = dict(request.query_args)
        page = query_dict.get('page') or 1
        page_size = query_dict.get('page_size') or 10
        datas = EmailSite.select().paginate(int(page), int(page_size))
        res_list = []
        for data in datas:
            res_list.append({'id': data.id,
                             'site_id': data.site_id,
                             'site_type': data.site_type,
                             'site_name': data.site_name,
                             'api_url': data.api_url,
                             'special': data.special})
        return json({
            "code": 1,
            "msg": "successful",
            "data": res_list
        })

