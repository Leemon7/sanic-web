# -*- coding: utf-8 -*-
# Created by: Leemon7
# Created on: 2021/11/15
# Function:
from sanic import Blueprint

from app.views.template import TemplateViews

blueprint_v2 = Blueprint('v2', url_prefix='/v2')

blueprint_v2.add_route(TemplateViews.as_view(), '/site/add/')
blueprint_v2.add_route(TemplateViews.as_view(), '/site/list/')