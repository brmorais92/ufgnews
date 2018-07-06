import aiohttp_jinja2
import aiohttp_session
import aiohttp

import views.index_view, views.login_view
import controllers.controller
import models.user.sqlite_dao, models.user.data, models.user.services
import models.article.sqlite_dao, models.article.data, models.article.services

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
            session['user'] = user.username
            return await views.login_view.handle(request, {})
        else:
            context = {'errors': []}
            context['errors'].append('Login ou senha inválidos')
            return await views.login_view.handle(request, context)

    @routes.get('/logout')
    async def logout_get(request):
        await models.article.services.ArticleServices(request).search_articles('primeira')
        session = await aiohttp_session.get_session(request)
        session.invalidate()
        raise aiohttp.web.HTTPFound('/')