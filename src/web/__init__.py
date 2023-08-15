from aiohttp import web, web_request
import os
def get_app():
    routes = web.RouteTableDef()

    ## 请求routes的根节点
    @routes.get("/")
    async def hello_world(request: web_request.Request):
        return web.Response(body=f"hello")


    ## 添加routes到app中
    app = web.Application()
    app.add_routes(routes)

    return app