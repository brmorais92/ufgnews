import aiohttp_jinja2
import aiohttp
from aiohttp_session import get_session
import controllers.controller
import models.user.sqlite_dao


class IndexController(controllers.controller.Controller):
    routes = aiohttp.web.RouteTableDef()
    @routes.get('/')
    @routes.get('/api')
    @aiohttp_jinja2.template('index.html')
    async def handle(request):
        #name = request.match_info.get('name', "Anonymous")
        session = await get_session(request)
        if 'user' in session:
            user = session['user']
        else:
            user = None
        return {'username': user}