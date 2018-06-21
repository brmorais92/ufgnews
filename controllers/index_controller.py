import aiohttp_jinja2
import aiohttp
from aiohttp_session import get_session
import controllers.controller


class IndexController(controllers.controller.Controller):
    routes = aiohttp.web.RouteTableDef()

    @routes.get('/')
    @routes.get('/api')
    @aiohttp_jinja2.template('index.html')
    async def handle(request):
        #name = request.match_info.get('name', "Anonymous")
        session = await get_session(request)
        if 'usuario' in session:
            user = session['usuario']
        else:
            user = None
        return {'username': user}