from aiohttp import web, web_request
from khl import Bot
def get_app():
    routes = web.RouteTableDef()

    ## 请求routes的根节点
    @routes.get("/")
    async def hello_world(request: web_request.Request):
        return web.Response(body=f"hello")

    @routes.post("/")
    async def post_index(request: web_request.Request):
        return web.Response(body=f"post")
    ## 添加routes到app中
    app = web.Application()
    app.add_routes(routes)

    return app