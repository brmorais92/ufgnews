import aiohttp_jinja2
import aiohttp_session
import aiohttp
import json

import views.index_view, views.login_view
import controllers.controller
import models.user.sqlite_dao, models.user.data, models.user.services


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
        user_service = models.user.services.UserServices(request)
        user_service.user = user
        if await user_service.login():
            session['user_id'] = user.id
            session['username'] = user.username
            session['password'] = user.password
            return await views.login_view.handle(request, {})
        else:
            context = {'errors': []}
            context['errors'].append('Login ou senha inválidos')
            return await views.login_view.handle(request, context)

    @routes.get('/logout')
    async def logout_get(request):
        session = await aiohttp_session.get_session(request)
        session.invalidate()
        raise aiohttp.web.HTTPFound('/')