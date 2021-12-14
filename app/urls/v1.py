# -*- coding: utf-8 -*-
# Created by: Leemon7
# Created on: 2021/11/15
# Function:

from sanic import Blueprint

from app.views.template import index

blueprint_v1 = Blueprint('v1', url_prefix='/v1')

blueprint_v1.add_route(index, '/', methods=['GET', 'POST'])