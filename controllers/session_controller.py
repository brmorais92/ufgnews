import aiohttp_jinja2
import aiohttp_session
import aiohttp

import views.index_view, views.login_view
import controllers.controller
import models.user.sqlite_dao, models.user.data


class SessionController(controllers.controller.Controller):

    routes = aiohttp.web.RouteTableDef()

    @routes.get('/login')
    async def login_get(request):
        return await views.login_view.handle(request, {})

    @routes.post('/login')
    async def login_post(request):
        session = await aiohttp_session.get_session(request)
        data = await request.post()
        user = models.user.data.User()
        user.username = data['username']
        user.password = data['password']
        if await models.user.sqlite_dao.fetch_user(request, user):
            session['user'] = user.username
            return await views.login_view.handle(request, {})
        else:
            context = {'errors': []}
            context['errors'].append('Falha no login')
            context['errors'].append('Segundo erro')
            return await views.login_view.handle(request, context)

    @routes.get('/logout')
    async def logout_get(request):
        session = await aiohttp_session.get_session(request)
        session.invalidate()
        raise aiohttp.web.HTTPFound('/')