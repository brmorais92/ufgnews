import aiohttp_jinja2
import aiohttp

from aiohttp_session import get_session
import controllers.controller


class IndexController(controllers.controller.Controller):
    routes = aiohttp.web.RouteTableDef()

    @routes.get('/')
    @aiohttp_jinja2.template('index.html')
    async def handle(request):
        session = await get_session(request)
        if 'username' in session:
            username = session['username']
        else:
            username = None
        return {'username': username}
