# -*- coding: utf-8 -*-
# Created by: Leemon7
# Created on: 2021/11/9
# Function:  web主入口


from sanic import Sanic
from app.urls.v1 import blueprint_v1
from app.urls.v2 import blueprint_v2

# 注册app实例，通过名称
app1 = Sanic(__name__)

# 通过名称检索app实例
app = Sanic.get_app(__name__)

# 注册蓝图
app.blueprint(blueprint_v1)
app.blueprint(blueprint_v2)


if __name__ == '__main__':
    # app.error_handler.add(NotFound, lambda r,e: sanic.response.empty(status=404))
    app.run(host='0.0.0.0', port=8000, workers=2)